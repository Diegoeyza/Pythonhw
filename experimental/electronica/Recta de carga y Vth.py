import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root_scalar
from scipy.interpolate import interp1d

def load_data(file_path):
    data = {}
    current_vgs = None
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if "Step Information" in line:
                # Parse Vgs value properly, handling both "mV" and "V"
                raw_value = line.split('=')[1].split()[0]
                if 'm' in raw_value:  # Millivolts
                    current_vgs = float(raw_value.replace('m', '')) / 1000
                else:  # Volts
                    current_vgs = float(raw_value)
                data[current_vgs] = {'vds': [], 'ids': []}
            elif line and current_vgs is not None:
                vds, ids = map(float, line.split())
                data[current_vgs]['vds'].append(vds)
                data[current_vgs]['ids'].append(ids)
    
    return data

def get_operating_point(data):
    # Display available Vgs values
    available_vgs = sorted(data.keys())
    print("\nAvailable Vgs values:")
    for i, vgs in enumerate(available_vgs, start=1):
        print(f"{i}: Vgs = {vgs:.2f} V")
    
    # Ask user to choose a Vgs
    while True:
        try:
            vgs_choice = int(input(f"Choose a Vgs by entering a number (1-{len(available_vgs)}): "))
            if 1 <= vgs_choice <= len(available_vgs):
                chosen_vgs = available_vgs[vgs_choice - 1]
                break
            else:
                print("Invalid choice. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Get the range of Vds for the selected Vgs
    vds_values = data[chosen_vgs]['vds']
    ids_values = data[chosen_vgs]['ids']
    vds_min, vds_max = min(vds_values), max(vds_values)
    
    print(f"\nFor Vgs = {chosen_vgs:.2f} V, the Vds range is:")
    print(f"Vds: {vds_min:.2f} V to {vds_max:.2f} V")
    
    # Ask user to specify Vds
    while True:
        try:
            desired_vds = float(input(f"Enter desired Vds (within {vds_min:.2f} to {vds_max:.2f} V): "))
            if vds_min <= desired_vds <= vds_max:
                # Find the closest matching Ids for the chosen Vds
                closest_idx = min(range(len(vds_values)), key=lambda i: abs(vds_values[i] - desired_vds))
                chosen_ids = ids_values[closest_idx]
                return (desired_vds, chosen_ids, chosen_vgs)
            else:
                print(f"Vds out of range. Please choose a value within {vds_min:.2f} to {vds_max:.2f} V.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_rd_and_plot(data, q_point):
    vds_q, ids_q, vgs_q = q_point
    vdd = float(input("Enter the supply voltage (Vdd): "))
    
    # Calculate RD
    rd = (vdd - vds_q) / ids_q if ids_q != 0 else float('inf')
    
    # Plotting
    plt.figure(figsize=(10, 6))
    for vgs, values in sorted(data.items()):
        plt.plot(values['vds'], values['ids'], label=f"Vgs = {vgs:.2f} V")
    
    # Load Line
    x_load = [0, vdd]
    y_load = [vdd / rd if rd != float('inf') else 0, 0]
    plt.plot(x_load, y_load, 'r--', label="Recta de Carga")
    
    # Mark Operating Point Q
    plt.scatter([vds_q], [ids_q], color='red', zorder=5, label=f"Q (Vds={vds_q:.2f}V, Ids={ids_q:.2f}A, Vgs={vgs_q:.2f}V)")
    
    plt.xlabel('Vds (V)')
    plt.ylabel('Ids (A)')
    plt.title('Recta de Carga')
    
    # Customize Legend
    plt.legend(loc='upper right', fontsize='small', frameon=True)  # Small font, positioned to the right
    plt.grid(True)
    plt.tight_layout()  # Ensure the layout fits well
    plt.show()
    
    print(f"\nOperating Point Q:")
    print(f"Vds = {vds_q:.2f} V, Ids = {ids_q:.2f} A, Vgs = {vgs_q:.2f} V")
    print(f"Calculated Resistance Rd = {rd:.2f} Ω")
    print(f"Vgs for this Q point is {vgs_q:.2f} V")
    
    # Return RD for further calculations
    return rd

def calculate_vth_from_curve(data, vgs_q):
    import numpy as np

    # Extract Vds and Ids for the chosen Vgs
    vds_values = np.array(data[vgs_q]['vds'])
    ids_values = np.array(data[vgs_q]['ids'])
    
    # Calculate slope (dIds/dVds)
    slopes = np.gradient(ids_values, vds_values)
    
    # Find the point where the slope transitions from near-zero to increasing
    threshold_index = None
    for idx in range(1, len(slopes)):
        if slopes[idx] == 0:  # Transition detected
            threshold_index = idx
            break
    
    if threshold_index is not None:
        # Get the Vds at the transition point
        vds_threshold = vds_values[threshold_index]
        vth = vgs_q - vds_threshold  # Calculate Vth
        
        # Print results
        print(f"\nThreshold Voltage Calculation for Vgs = {vgs_q:.2f} V:")
        print(f"Transition point found at Vds = {vds_threshold:.2f} V")
        print(f"Calculated Vth = {vth:.2f} V")
        
        return vth
    else:
        print("Unable to find a clear transition point in the curve.")
        return None


def calculate_ro(data, vgs_q):
    import numpy as np

    # Extract Vds and Ids for the chosen Vgs
    vds_values = np.array(data[vgs_q]['vds'])
    ids_values = np.array(data[vgs_q]['ids'])
    
    # Calculate slope (dIds/dVds) for the active region
    slopes = np.gradient(ids_values, vds_values)
    
    # Identify the active region (where Vds > Vds_threshold)
    threshold_index = None
    for idx in range(1, len(slopes)):
        if slopes[idx] == 0:  # Transition detected
            threshold_index = idx
            break
    
    if threshold_index is not None:
        # Focus on the active region (beyond the threshold point)
        active_vds = vds_values[threshold_index:]
        active_slopes = slopes[threshold_index:]
        
        # Calculate ro as 1/(average slope) in the active region
        avg_slope = np.mean(active_slopes)
        ro = 1 / avg_slope if avg_slope != 0 else float('inf')
        
        print(f"\nOutput Resistance (ro) for Vgs = {vgs_q:.2f} V:")
        print(f"ro = {ro:.2f} Ω (calculated in the active region)")
        
        return ro
    else:
        print("Unable to calculate ro: No clear active region detected.")
        return None

def calculate_gm(data, vgs_q):
    import numpy as np

    # Sort the Vgs values to find neighbors of the selected Vgs
    vgs_values = sorted(data.keys())
    idx = vgs_values.index(vgs_q)
    
    if idx > 0 and idx < len(vgs_values) - 1:
        # Use neighboring Vgs values for numerical differentiation
        vgs_prev, vgs_next = vgs_values[idx - 1], vgs_values[idx + 1]
        ids_prev = np.mean(data[vgs_prev]['ids'])  # Average Ids at previous Vgs
        ids_next = np.mean(data[vgs_next]['ids'])  # Average Ids at next Vgs
        
        # Calculate gm as (delta Ids) / (delta Vgs)
        gm = (ids_next - ids_prev) / (vgs_next - vgs_prev)
        
        print(f"\nTransconductance (gm) for Vgs = {vgs_q:.2f} V:")
        print(f"gm = {gm:.2f} S (calculated using neighboring Vgs values)")
        
        return gm
    else:
        print("Unable to calculate gm: Insufficient neighboring Vgs values.")
        return None

def estimate_max_vgs_before_triode(data, rd, vth, vdd):
    """
    Estimate the maximum Vgs before the transistor enters the triode region.
    """
    max_vgs = None

    # Generate a fine-resolution load line
    vds_load = np.linspace(0, vdd, 1000)
    ids_load = (vdd - vds_load) / rd if rd != float('inf') else np.zeros_like(vds_load)

    for vgs, values in sorted(data.items()):
        if vgs <= vth:
            continue  # Skip Vgs values below the threshold
        
        vds_values = np.array(values['vds'])
        ids_values = np.array(values['ids'])
        
        # Define the difference function to find the intersection
        def difference(vds):
            ids_device = np.interp(vds, vds_values, ids_values)
            ids_loadline = np.interp(vds, vds_load, ids_load)
            return ids_device - ids_loadline

        # Find the intersection point using numerical root-finding
        try:
            result = root_scalar(difference, bracket=(0, vdd), method='brentq')
            if result.converged:
                vds_intersect = result.root
                ids_intersect = np.interp(vds_intersect, vds_values, ids_values)

                # Verify if the intersection is in the triode region
                if vds_intersect < (vgs - vth):
                    # Calculate slope to confirm triode
                    idx = np.searchsorted(vds_values, vds_intersect)
                    if idx < len(vds_values) - 1:
                        slope = (ids_values[idx + 1] - ids_values[idx]) / (vds_values[idx + 1] - vds_values[idx])
                        if slope > 0:
                            max_vgs = vgs
                            print(f"Critical Vgs = {max_vgs:.2f} V")
                            print(f"Critical Vds = {vds_intersect:.2f} V, Ids = {ids_intersect:.2f} A")

                            # Plot the curves and critical point
                            plt.figure(figsize=(10, 6))
                            for vgs_key, curve in sorted(data.items()):
                                plt.plot(curve['vds'], curve['ids'], label=f"Vgs = {vgs_key:.2f} V")
                            
                            plt.plot(vds_load, ids_load, 'r--', label="Recta de Carga")
                            plt.scatter([vds_intersect], [ids_intersect], color='orange', zorder=5,
                                        label=f"Critical Point (Vgs={max_vgs:.2f}V, Vds={vds_intersect:.2f}V)")
                            
                            plt.xlabel('Vds (V)')
                            plt.ylabel('Ids (A)')
                            plt.title('Recta de Carga y Punto Crítico')
                            plt.legend(loc='upper right', fontsize='small', frameon=True)
                            plt.grid(True)
                            plt.tight_layout()
                            plt.show()
                            return max_vgs
        except ValueError:
            # Skip if no valid intersection is found in the bracket range
            pass

    print("No se encontró un valor crítico de Vgs antes de entrar en la región de triodo.")
    return max_vgs

def calculate_max_vgs_with_loadline(data, rd, vth, vdd, q_point):
    """
    Calculate the maximum Vgs before entering the triode region by generating 
    interpolated Vgs curves. Ensures Point B is valid with respect to the load line.
    """
    import numpy as np
    from scipy.interpolate import interp1d
    from scipy.optimize import root_scalar

    vds_q, ids_q, vgs_q = q_point
    vgs_values = sorted(data.keys())
    current_idx = vgs_values.index(vgs_q)
    
    # Initial points and data for curves
    current_curve = vgs_values[current_idx]
    vds_current = np.array(data[current_curve]['vds'])
    ids_current = np.array(data[current_curve]['ids'])

    # Function to find the saturation transition (triode -> saturation)
    def find_transition(vds, ids):
        slopes = np.gradient(ids, vds)
        transition_idx = np.argmax(slopes <= 0)
        return vds[transition_idx], ids[transition_idx]

    # Find Point A
    point_a_vds, point_a_ids = find_transition(vds_current, ids_current)

    # Load line calculation
    vds_load = np.linspace(0, vdd, 1000)
    ids_load = (vdd - vds_load) / rd if rd != float('inf') else np.zeros_like(vds_load)

    def is_valid_point(vds_point, ids_point):
        # Check if the load line at the given Vds is to the left of the point
        ids_at_vds = np.interp(vds_point, vds_load, ids_load)
        return ids_at_vds <= ids_point

    # Iterate over higher Vgs values to find a valid Point B
    for next_idx in range(current_idx + 1, len(vgs_values)):
        next_curve = vgs_values[next_idx]
        vds_next = np.array(data[next_curve]['vds'])
        ids_next = np.array(data[next_curve]['ids'])

        # Find Point B
        point_b_vds, point_b_ids = find_transition(vds_next, ids_next)

        if is_valid_point(point_b_vds, point_b_ids):
            break  # Found a valid Point B
        else:
            # Redefine Point A as Point B and continue
            point_a_vds, point_a_ids = point_b_vds, point_b_ids
            vds_current, ids_current = vds_next, ids_next
    else:
        raise ValueError("Could not find a valid Point B in the available data.")

    # Generate artificial curves between Point A and Point B
    vgs_steps = np.linspace(current_curve, next_curve, num=200)
    artificial_curves = []

    for step, vgs_interpolated in enumerate(vgs_steps[1:], start=1):
        alpha = step / len(vgs_steps)
        vds_interpolated = np.linspace(0, vdd, len(vds_current))  # Generate Vds grid
        ids_interpolated = (
            (1 - alpha) * np.interp(vds_interpolated, vds_current, ids_current) +
            alpha * np.interp(vds_interpolated, vds_next, ids_next)
        )
        artificial_curves.append((vgs_interpolated, vds_interpolated, ids_interpolated))

    # Determine the last artificial curve in saturation region
    vgs_critical = None
    intersection_point = None

    for vgs_interpolated, vds_interpolated, ids_interpolated in artificial_curves:
        # Intersect with load line
        def difference(vds):
            ids_device = np.interp(vds, vds_interpolated, ids_interpolated)
            ids_loadline = np.interp(vds, vds_load, ids_load)
            return ids_device - ids_loadline

        try:
            result = root_scalar(difference, bracket=(0, vdd), method='brentq')
            if result.converged:
                vds_intersect = result.root
                ids_intersect = np.interp(vds_intersect, vds_interpolated, ids_interpolated)

                # Check if intersection point is in saturation
                if vds_intersect >= (vgs_interpolated - vth):
                    vgs_critical = vgs_interpolated
                    intersection_point = (vds_intersect, ids_intersect)
                else:
                    break
        except ValueError:
            pass

    # Plot all curves, including artificial and original
    plt.figure(figsize=(10, 6))
    
    # Original Vgs curves
    for vgs, curve in sorted(data.items()):
        plt.plot(curve['vds'], curve['ids'], label=f"Original Vgs = {vgs:.2f} V")
    
    # Artificial curves
    for vgs_interpolated, vds_interpolated, ids_interpolated in artificial_curves:
        plt.plot(vds_interpolated, ids_interpolated, '--')
    
    # Load line
    plt.plot(vds_load, ids_load, 'r--', label="Load Line")
    
    # Mark intersection point
    if intersection_point:
        plt.scatter([intersection_point[0]], [intersection_point[1]], color='orange', zorder=5,
                    label=f"Critical Point (Vgs={vgs_critical:.2f}V, Vds={intersection_point[0]:.2f}V)")
    
    plt.xlabel('Vds (V)')
    plt.ylabel('Ids (A)')
    plt.title('Interpolated Vgs Curves and Load Line Intersection')
    plt.legend(loc='upper right', fontsize='small', frameon=True)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print(f"Critical Vgs = {vgs_critical:.2f} V")
    return vgs_critical


def calculate_max_vgs_with_loadline_focused(data, rd, vth, vdd, q_point):
    """
    Calculate the maximum Vgs before entering the triode region by generating 
    interpolated Vgs curves. Ensures Point B is valid with respect to the load line.
    Only plots the selected artificial curve with the original curves.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.interpolate import interp1d
    from scipy.optimize import root_scalar

    vds_q, ids_q, vgs_q = q_point
    vgs_values = sorted(data.keys())
    current_idx = vgs_values.index(vgs_q)
    
    # Initial points and data for curves
    current_curve = vgs_values[current_idx]
    vds_current = np.array(data[current_curve]['vds'])
    ids_current = np.array(data[current_curve]['ids'])

    # Function to find the saturation transition (triode -> saturation)
    def find_transition(vds, ids):
        slopes = np.gradient(ids, vds)
        transition_idx = np.argmax(slopes <= 0)
        return vds[transition_idx], ids[transition_idx]

    # Find Point A
    point_a_vds, point_a_ids = find_transition(vds_current, ids_current)

    # Load line calculation
    vds_load = np.linspace(0, vdd, 1000)
    ids_load = (vdd - vds_load) / rd if rd != float('inf') else np.zeros_like(vds_load)

    def is_valid_point(vds_point, ids_point):
        # Check if the load line at the given Vds is to the left of the point
        ids_at_vds = np.interp(vds_point, vds_load, ids_load)
        return ids_at_vds <= ids_point

    # Iterate over higher Vgs values to find a valid Point B
    for next_idx in range(current_idx + 1, len(vgs_values)):
        next_curve = vgs_values[next_idx]
        vds_next = np.array(data[next_curve]['vds'])
        ids_next = np.array(data[next_curve]['ids'])

        # Find Point B
        point_b_vds, point_b_ids = find_transition(vds_next, ids_next)

        if is_valid_point(point_b_vds, point_b_ids):
            break  # Found a valid Point B
        else:
            # Redefine Point A as Point B and continue
            point_a_vds, point_a_ids = point_b_vds, point_b_ids
            vds_current, ids_current = vds_next, ids_next
    else:
        raise ValueError("Could not find a valid Point B in the available data.")

    # Generate artificial curves between Point A and Point B
    vgs_steps = np.linspace(current_curve, next_curve, num=20)
    artificial_curves = []

    for step, vgs_interpolated in enumerate(vgs_steps[1:], start=1):
        alpha = step / len(vgs_steps)
        vds_interpolated = np.linspace(0, vdd, len(vds_current))  # Generate Vds grid
        ids_interpolated = (
            (1 - alpha) * np.interp(vds_interpolated, vds_current, ids_current) +
            alpha * np.interp(vds_interpolated, vds_next, ids_next)
        )
        artificial_curves.append((vgs_interpolated, vds_interpolated, ids_interpolated))

    # Determine the last artificial curve in saturation region
    vgs_critical = None
    intersection_point = None
    selected_curve = None

    for vgs_interpolated, vds_interpolated, ids_interpolated in artificial_curves:
        # Intersect with load line
        def difference(vds):
            ids_device = np.interp(vds, vds_interpolated, ids_interpolated)
            ids_loadline = np.interp(vds, vds_load, ids_load)
            return ids_device - ids_loadline

        try:
            result = root_scalar(difference, bracket=(0, vdd), method='brentq')
            if result.converged:
                vds_intersect = result.root
                ids_intersect = np.interp(vds_intersect, vds_interpolated, ids_interpolated)

                # Check if intersection point is in saturation
                if vds_intersect >= (vgs_interpolated - vth):
                    vgs_critical = vgs_interpolated
                    intersection_point = (vds_intersect, ids_intersect)
                    selected_curve = (vgs_interpolated, vds_interpolated, ids_interpolated)
                else:
                    break
        except ValueError:
            pass

    if not selected_curve:
        raise ValueError("No valid artificial curve found that remains in saturation.")

    # Plot original curves
    plt.figure(figsize=(10, 6))
    for vgs, curve in sorted(data.items()):
        plt.plot(curve['vds'], curve['ids'], label=f"Original Vgs = {vgs:.2f} V")

    # Plot the selected artificial curve
    vgs_interpolated, vds_interpolated, ids_interpolated = selected_curve
    plt.plot(vds_interpolated, ids_interpolated, '--', label=f"Selected Artificial Vgs = {vgs_critical:.2f} V")

    # Load line
    plt.plot(vds_load, ids_load, 'r--', label="Load Line")

    # Mark intersection point
    if intersection_point:
        plt.scatter([intersection_point[0]], [intersection_point[1]], color='orange', zorder=5,
                    label=f"Critical Point (Vgs={vgs_critical:.2f}V, Vds={intersection_point[0]:.2f}V)")
    
    plt.xlabel('Vds (V)')
    plt.ylabel('Ids (A)')
    plt.title('Interpolated Vgs Curve and Load Line Intersection')
    plt.legend(loc='upper right', fontsize='small', frameon=True)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Print critical values
    print(f"Selected Artificial Curve:")
    print(f"  Vgs = {vgs_critical:.2f} V")
    print(f"  Vds = {intersection_point[0]:.2f} V")
    print(f"  Ids = {intersection_point[1]:.2e} A")
    
    return vgs_critical, intersection_point




# File path
file_path = r"C:\Users\diego\Downloads\Draft1.txt"

# Main Execution
data = load_data(file_path)
q_point = get_operating_point(data)
rd = calculate_rd_and_plot(data, q_point)
vth = calculate_vth_from_curve(data, q_point[2])
critical_vgs = estimate_max_vgs_before_triode(data, rd, vth, vdd=float(10))
critical_vgs = calculate_max_vgs_with_loadline(data, rd, vth, 10, q_point)
critical_vgs = calculate_max_vgs_with_loadline_focused(data, rd, vth, 10, q_point)
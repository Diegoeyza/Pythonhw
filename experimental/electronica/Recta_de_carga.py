import matplotlib.pyplot as plt

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




# File path
file_path = r"C:\Users\diego\Downloads\Draft1.txt"

data = load_data(file_path)
q_point = get_operating_point(data)
calculate_rd_and_plot(data, q_point)
vth = calculate_vth_from_curve(data, q_point[2])
ro = calculate_ro(data, q_point[2])
gm = calculate_gm(data, q_point[2])

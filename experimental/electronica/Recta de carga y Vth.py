import matplotlib.pyplot as plt
import numpy as np

def load_data(file_path):
    data = {}
    current_vgs = None

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if "Step Information" in line:
                raw_value = line.split('=')[1].split()[0]
                if 'm' in raw_value:
                    current_vgs = float(raw_value.replace('m', '')) / 1000
                else:
                    current_vgs = float(raw_value)
                data[current_vgs] = {'vds': [], 'ids': []}
            elif line and current_vgs is not None:
                vds, ids = map(float, line.split())
                data[current_vgs]['vds'].append(vds)
                data[current_vgs]['ids'].append(ids)

    return data

def find_active_region_points(data):
    active_points = []
    for vgs, values in sorted(data.items()):
        vds = np.array(values['vds'])
        ids = np.array(values['ids'])
        slopes = np.diff(ids) / np.diff(vds)
        for i, slope in enumerate(slopes):
            if abs(slope) < 1e-3:
                active_points.append((vds[i], ids[i], vgs))
    return active_points

def get_operating_point(active_points):
    vds_min = min(point[0] for point in active_points)
    vds_max = max(point[0] for point in active_points)
    ids_min = min(point[1] for point in active_points)
    ids_max = max(point[1] for point in active_points)

    print(f"\nSelectable Range for Operating Point Q (Active Region Only):")
    print(f"Vds: {vds_min:.2f} V to {vds_max:.2f} V")
    print(f"Ids: {ids_min:.2f} A to {ids_max:.2f} A\n")

    while True:
        try:
            desired_vds = float(input(f"Enter desired Vds (within {vds_min:.2f} to {vds_max:.2f} V): "))
            desired_ids = float(input(f"Enter desired Ids (within {ids_min:.2f} to {ids_max:.2f} A): "))

            closest_point = min(active_points, key=lambda x: abs(x[0] - desired_vds) + abs(x[1] - desired_ids))
            return closest_point
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

def calculate_rd_and_plot(data, q_point):
    vds_q, ids_q, vgs_q = q_point
    vdd = float(input("Enter the supply voltage (Vdd): "))

    rd = (vdd - vds_q) / ids_q if ids_q != 0 else float('inf')

    plt.figure(figsize=(10, 6))
    for vgs, values in sorted(data.items()):
        plt.plot(values['vds'], values['ids'], label=f"Vgs = {vgs:.2f} V")

    x_load = [0, vdd]
    y_load = [vdd / rd if rd != float('inf') else 0, 0]
    plt.plot(x_load, y_load, 'r--', label="Recta de Carga")

    plt.scatter([vds_q], [ids_q], color='red', zorder=5, label=f"Q (Vds={vds_q:.2f}V, Ids={ids_q:.2f}A, Vgs={vgs_q:.2f}V)")

    plt.xlabel('Vds (V)')
    plt.ylabel('Ids (A)')
    plt.title('Recta de Carga')
    plt.legend(loc='upper right', fontsize='small', frameon=True)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print(f"\nOperating Point Q:")
    print(f"Vds = {vds_q:.2f} V, Ids = {ids_q:.2f} A, Vgs = {vgs_q:.2f} V")
    print(f"Calculated Resistance Rd = {rd:.2f} Ω")
    print(f"Vgs for this Q point is {vgs_q:.2f} V")

    return rd

def estimate_max_vgs(data, q_point):
    vds_q, ids_q, vgs_q = q_point
    higher_vgs_curves = [vgs for vgs in sorted(data.keys()) if vgs > vgs_q]

    slopes_at_q = []
    for vgs in higher_vgs_curves:
        vds = np.array(data[vgs]['vds'])
        ids = np.array(data[vgs]['ids'])
        if vds_q in vds:
            idx = np.where(vds == vds_q)[0][0]
            if idx < len(vds) - 1:
                slope = (ids[idx + 1] - ids[idx]) / (vds[idx + 1] - vds[idx])
                slopes_at_q.append((vgs, slope))

    if slopes_at_q:
        for i, (vgs, slope) in enumerate(slopes_at_q):
            if abs(slope) > 1e-3:
                if i == 0:
                    print(f"\nEstimated max Vgs before triode: {vgs:.2f} V")
                else:
                    vgs_prev, slope_prev = slopes_at_q[i - 1]
                    slope_rate = (slope - slope_prev) / (vgs - vgs_prev)
                    estimated_vgs = vgs_prev + (1e-3 - slope_prev) / slope_rate
                    print(f"\nEstimated max Vgs before triode: {estimated_vgs:.2f} V (Extrapolated)")
                break
        else:
            print("\nAll higher Vgs curves remain near the active region.")
    else:
        print("\nNo valid higher Vgs curves found for estimation.")

# File path
file_path = r"C:\Users\diego\Downloads\Draft1.txt"

data = load_data(file_path)
active_points = find_active_region_points(data)
q_point = get_operating_point(active_points)
rd = calculate_rd_and_plot(data, q_point)

# Optional step
if input("\nDo you want to estimate the maximum Vgs before entering triode? (yes/no): ").strip().lower() == 'yes':
    estimate_max_vgs(data, q_point)

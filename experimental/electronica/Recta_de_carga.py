import matplotlib.pyplot as plt

def load_data(file_path):
    data = {}
    current_vgs = None
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if "Step Information" in line:
                current_vgs = float(line.split('=')[1].split()[0].replace('m', '')) / 1000 if 'm' in line else float(line.split('=')[1].split()[0])
                data[current_vgs] = {'vds': [], 'ids': []}
            elif line and current_vgs is not None:
                vds, ids = map(float, line.split())
                data[current_vgs]['vds'].append(vds)
                data[current_vgs]['ids'].append(ids)
    
    return data

def get_operating_point(data):
    points = []
    for vgs, values in sorted(data.items()):
        for vds, ids in zip(values['vds'], values['ids']):
            points.append((vds, ids, vgs))
    points = sorted(points, key=lambda x: (x[0], x[1]))  # Sort by Vds and Ids
    
    print("Available Operating Points (Index, Vds, Ids, Vgs):")
    for i, (vds, ids, vgs) in enumerate(points):
        print(f"{i}: Vds = {vds:.2f} V, Ids = {ids:.2f} A, Vgs = {vgs:.2f} V")
    
    idx = int(input("Select an index for the operating point Q: "))
    return points[idx]

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
    plt.scatter([vds_q], [ids_q], color='red', zorder=5, label=f"Q (Vds={vds_q:.2f}V, Ids={ids_q:.2f}A)")
    
    plt.xlabel('Vds (V)')
    plt.ylabel('Ids (A)')
    plt.title('Recta de Carga')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"\nOperating Point Q:")
    print(f"Vds = {vds_q:.2f} V, Ids = {ids_q:.2f} A, Vgs = {vgs_q:.2f} V")
    print(f"Calculated Resistance Rd = {rd:.2f} Ω")
    print(f"Vgs for this Q point is {vgs_q:.2f} V")

# File path
file_path = r"C:\Users\diego\Downloads\Vgs_lab.txt"

data = load_data(file_path)
q_point = get_operating_point(data)
calculate_rd_and_plot(data, q_point)

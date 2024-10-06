import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

# Load the data from the CSV file
file_path = r"experimental\electronica\SDS00006.CSV"
data = pd.read_csv(file_path, skiprows=1)  # Skip the header row with 'Second,Volt,Volt'

# Strip any leading or trailing whitespace from column names
data.columns = data.columns.str.strip()

# Interpolation to make curves sharper
x = data['Second']
y1 = (data['Volt'])
y2 = (data['Volt.1'])

# Interpolation with 300 points for smoother curves
x_new = np.linspace(x.min(), x.max(), 300)
spl1 = make_interp_spline(x, y1, k=3)  # k=3 for cubic spline
spl2 = make_interp_spline(x, y2, k=3)

y1_smooth = spl1(x_new)
y2_smooth = spl2(x_new)

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(x_new, y1_smooth, label='In (CH1)', marker='')
plt.plot(x_new, y2_smooth, label='Out (CH2)', marker='')
plt.title('Voltage vs Time')
plt.xlabel('Time (s)')
#plt.xlim(-0.04, 0.04)
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

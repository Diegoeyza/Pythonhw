import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

def plot_voltage_vs_time_ch1_ch2(file_ch1, file_ch2):
    """
    Plots Voltage vs. Time for two channels from two separate CSV files.
    Smooths the curves using cubic spline interpolation.

    Args:
        file_ch1 (str): Path to the CSV file for Channel 1.
        file_ch2 (str): Path to the CSV file for Channel 2.
    """
    # Load the data from Channel 1
    data_ch1 = pd.read_csv(file_ch1, skiprows=0, header=None)
    data_ch1 = data_ch1.dropna(axis=1, how='all')  # Drop empty columns
    data_ch1 = data_ch1.iloc[:, -2:]  # Select the last two columns with data
    data_ch1.columns = ['Time', 'Voltage']  # Rename columns
    data_ch1 = data_ch1.apply(pd.to_numeric, errors='coerce').dropna()  # Ensure numeric data

    # Load the data from Channel 2
    data_ch2 = pd.read_csv(file_ch2, skiprows=0, header=None)
    data_ch2 = data_ch2.dropna(axis=1, how='all')  # Drop empty columns
    data_ch2 = data_ch2.iloc[:, -2:]  # Select the last two columns with data
    data_ch2.columns = ['Time', 'Voltage']  # Rename columns
    data_ch2 = data_ch2.apply(pd.to_numeric, errors='coerce').dropna()  # Ensure numeric data

    # Interpolation for Channel 1
    time_ch1 = data_ch1['Time']
    voltage_ch1 = data_ch1['Voltage']
    time_ch1_smooth = np.linspace(time_ch1.min(), time_ch1.max(), 300)
    spline_ch1 = make_interp_spline(time_ch1, voltage_ch1, k=3)
    voltage_ch1_smooth = spline_ch1(time_ch1_smooth)

    # Interpolation for Channel 2
    time_ch2 = data_ch2['Time']
    voltage_ch2 = data_ch2['Voltage']
    time_ch2_smooth = np.linspace(time_ch2.min(), time_ch2.max(), 300)
    spline_ch2 = make_interp_spline(time_ch2, voltage_ch2, k=3)
    voltage_ch2_smooth = spline_ch2(time_ch2_smooth)

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(time_ch1_smooth, voltage_ch1_smooth, label='Channel 1', marker='', color='blue')
    plt.plot(time_ch2_smooth, voltage_ch2_smooth, label='Channel 2', marker='', color='orange')
    plt.title('Voltage vs Time (2KHz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

# Example usage
# Replace the file paths with the paths to your Channel 1 and Channel 2 CSV files
plot_voltage_vs_time_ch1_ch2(r"C:\Users\diego\Downloads\CH1 2KHZ.CSV", r"C:\Users\diego\Downloads\CH2 2KHZ.CSV")

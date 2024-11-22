import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
def read_csv(file_path):
    # Load the CSV file and select only the last two columns (time and voltage)
    data = pd.read_csv(file_path)
    time = data.iloc[:, -3]  # Assuming time is the second-to-last column
    voltage = data.iloc[:, -2]  # Assuming voltage is the last column
    return time, voltage

# Perform FFT on a portion of the data
def compute_fft(time, voltage, time_percentage):
    # Determine the indices based on the selected percentage
    n_total = len(time)
    n_selected = int(n_total * (time_percentage / 100))
    
    # Select the portion of the data
    time_selected = time[:n_selected]
    voltage_selected = voltage[:n_selected]
    
    # Calculate the sampling frequency
    fs = 1 / (time_selected.iloc[1] - time_selected.iloc[0])  # Assuming uniform sampling rate
    # Perform the FFT
    n = len(voltage_selected)
    freq = np.fft.fftfreq(n, d=(time_selected.iloc[1] - time_selected.iloc[0]))  # Frequency bins
    fft_values = np.fft.fft(voltage_selected)  # FFT of the signal
    fft_amplitude = np.abs(fft_values)  # Magnitude of the FFT
    return freq, fft_amplitude, time_selected

# Plot the results
def plot_fft(freq, fft_amplitude):
    plt.figure(figsize=(10, 6))
    plt.plot(freq[:len(freq)//2], fft_amplitude[:len(freq)//2])  # Plot only the positive frequencies
    plt.title('FFT of Voltage Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# Main function
def main(file_path, time_percentage=100):
    time, voltage = read_csv(file_path)
    freq, fft_amplitude, time_selected = compute_fft(time, voltage, time_percentage)
    
    # Print the time range based on the selected percentage
    print(f"Using {time_percentage}% of the data from time: {time_selected.iloc[0]} to {time_selected.iloc[-1]}")
    
    plot_fft(freq, fft_amplitude)

# Usage
file_path = r"C:\Users\diego\Downloads\F0037CH1.CSV"
time_percentage = 10  # Specify the percentage of the time to use (e.g., 50%)
main(file_path, time_percentage)




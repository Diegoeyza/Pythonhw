import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import windows

# Function to perform FFT and plot the graph
def plot_fft(time, voltages1, voltages2=None, channel1='CH1', channel2='CH2'):
    N = len(voltages1)  # Number of data points
    T = np.mean(np.diff(time))  # Sampling period (mean of time differences)

    # Remove DC component (subtract mean from signal)
    voltages1 -= np.mean(voltages1)
    if voltages2 is not None:
        voltages2 -= np.mean(voltages2)

    # Apply a window function (Hamming window to reduce spectral leakage)
    window = windows.hamming(N)
    voltages1_windowed = voltages1 * window
    if voltages2 is not None:
        voltages2_windowed = voltages2 * window

    # Perform FFT on the windowed signal
    yf1 = fft(voltages1_windowed)
    xf = fftfreq(N, T)[:N//2]  # Frequency axis
    amplitudes1 = 2.0/N * np.abs(yf1[:N//2])  # Amplitudes for channel 1

    # Find the index of the maximum amplitude for channel 1
    max_index1 = np.argmax(amplitudes1)
    max_freq1 = xf[max_index1]  # Frequency corresponding to max amplitude for channel 1

    # Create a plot
    plt.figure(figsize=(10, 6))

    # Plot for channel 1
    plt.plot(xf, amplitudes1, label=channel1)

    if voltages2 is not None:
        # FFT for channel 2
        voltages2_windowed = voltages2 * window
        yf2 = fft(voltages2_windowed)
        amplitudes2 = 2.0/N * np.abs(yf2[:N//2])  # Amplitudes for channel 2

        # Find the index of the maximum amplitude for channel 2
        max_index2 = np.argmax(amplitudes2)
        max_freq2 = xf[max_index2]  # Frequency corresponding to max amplitude for channel 2
        
        # Plot for channel 2
        plt.plot(xf, amplitudes2, label=channel2)

        # Determine the maximum frequency to set x-axis limit
        max_freq = 250#max(max_freq1, max_freq2)
    else:
        # Set the x-axis limit to 10 times the max frequency for a single channel
        max_freq = max_freq1

    # Set x-axis limit
    plt.xlim(0, max_freq * 10)  # Set limit to 10 times the max frequency
    
    # Plot settings
    plt.title('FFT of Voltage')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (V)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Step 1: Load the data from CSV
filename = r"C:\Users\diego\Github\ECG_project\ECG normal.CSV"
df = pd.read_csv(filename, skiprows=1)

# Step 2: Choose which channels to analyze
channel_choice = input("Choose the channel to analyze (CH1, CH2, or BOTH) (CH1 is in and CH2 is out): ").strip().upper()

if channel_choice == "CH1" or channel_choice == "1":
    voltages1 = df['Volt']
    channel1 = "Input"
    voltages2 = None
    channel2 = None
elif channel_choice == "CH2" or channel_choice == "2":
    voltages1 = df['Volt.1']
    channel1 = "Output"
    voltages2 = None
    channel2 = None
elif channel_choice == "BOTH" or "b":
    voltages1 = df['Volt']
    channel1 = "Input"
    voltages2 = df['Volt.1']
    channel2 = "Output"
else:
    raise ValueError("Invalid choice! Please choose either CH1, CH2, or BOTH.")

# Step 3: Extract time and corresponding voltage data
time = df['Second']

# Step 4: Plot the FFT result for the chosen channel(s)
plot_fft(time, voltages1, voltages2, channel1, channel2)

import matplotlib.pyplot as plt
import csv

def plot_fft_from_csv(file_path):
    """
    Reads a CSV file containing FFT data and plots the time vs frequency graph.
    
    Args:
        file_path (str): Path to the CSV file.
    """
    times = []
    frequencies = []
    
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Skip rows that don't have at least two columns with numerical data
            if len(row) < 5 or not row[3].strip() or not row[4].strip():
                continue
            
            try:
                time = float(row[3])
                frequency = float(row[4])
                times.append(time)
                frequencies.append(frequency)
            except ValueError:
                # Skip rows with non-numeric data in relevant columns
                continue
    
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(times, frequencies, label="FFT Data")
    plt.title("FFT: Time vs Frequency")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.legend()
    plt.grid(True)
    plt.show()

import matplotlib.pyplot as plt
import csv

def plot_fft_from_two_csvs_min_aligned(file_path1, file_path2, time_percentage=100):
    """
    Reads two CSV files containing FFT data and plots their time vs frequency graphs together,
    aligning both datasets so their frequencies start at the minimum value (baseline 0 Hz).
    
    Args:
        file_path1 (str): Path to the first CSV file (labeled as CH1).
        file_path2 (str): Path to the second CSV file (labeled as CH2).
        time_percentage (float): Percentage of the time data to use (0-100). Defaults to 100 (all data).
    """
    def extract_data(file_path):
        """Helper function to extract time and frequency data from a CSV file."""
        times = []
        frequencies = []
        
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Skip rows that don't have at least two columns with numerical data
                if len(row) < 5 or not row[3].strip() or not row[4].strip():
                    continue
                
                try:
                    time = float(row[3])
                    frequency = float(row[4])
                    times.append(time)
                    frequencies.append(frequency)
                except ValueError:
                    # Skip rows with non-numeric data in relevant columns
                    continue
        
        return times, frequencies

    # Extract data from both files
    times1, frequencies1 = extract_data(file_path1)
    times2, frequencies2 = extract_data(file_path2)

    # Determine the amount of data to use based on the time percentage
    if 0 < time_percentage <= 100:
        n1 = int(len(times1) * (time_percentage / 100))
        n2 = int(len(times2) * (time_percentage / 100))
        
        times1 = times1[:n1]
        frequencies1 = frequencies1[:n1]
        times2 = times2[:n2]
        frequencies2 = frequencies2[:n2]

    # Align frequencies based on the minimum value
    if frequencies1 and frequencies2:
        min_freq1 = min(frequencies1)  # Minimum frequency value of CH1
        min_freq2 = min(frequencies2)  # Minimum frequency value of CH2
        
        frequencies1 = [freq - min_freq1 for freq in frequencies1]
        frequencies2 = [freq - min_freq2 for freq in frequencies2]

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(times1, frequencies1, label="CH1", color="blue", alpha=0.7)
    plt.plot(times2, frequencies2, label="CH2", color="orange", alpha=0.7)
    plt.title(f"FFT: Frequency vs Voltage (50Hz)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (mV)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Usage example (replace with actual file paths and desired time percentage):
plot_fft_from_two_csvs_min_aligned(r'experimental\electronica\fft CSV\data\50_fft_CH1.CSV', r'experimental\electronica\fft CSV\data\50_fft_CH2.CSV', time_percentage=4)


# Usage example (replace 'path/to/your/file.csv' with the actual path)
#plot_fft_from_csv(r'experimental\electronica\fft CSV\data\50_fft_CH1.CSV')

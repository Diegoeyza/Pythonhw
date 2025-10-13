import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# --- Load CSV ---
file = r"C:\Users\diego\Github\Pythonhw\signals_GT.csv"
df = pd.read_csv(file)
fsrii = df['FSRII'].dropna().to_numpy()
ecg = df['ECG'].dropna().to_numpy()

# --- Detect peaks ---
fsrii_peaks, _ = find_peaks(fsrii, height=np.mean(fsrii)+0.1*np.std(fsrii), distance=20)
ecg_peaks, _ = find_peaks(ecg, height=np.mean(ecg)+0.3*np.std(ecg), distance=50)

# --- 1️⃣ Overlay plot: ECG peaks aligned with FSRII peaks ---
plt.figure(figsize=(12,4))
plt.plot(fsrii, label='FSRII', linewidth=1)
plt.plot(ecg, label='ECG', linewidth=1)
plt.plot(fsrii_peaks, fsrii[fsrii_peaks], 'ro', label='FSRII Peaks')
plt.plot(ecg_peaks, ecg[ecg_peaks], 'kx', label='ECG Peaks')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.title('FSRII and ECG with Peaks')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 2️⃣ Compute cumulative coupling ---
# Define a window (in samples) to consider a peak "coupled"
window = 20  # adjust depending on your sampling rate

# For each FSRII peak, check if an ECG peak is within +/- window
coupled = np.zeros_like(fsrii_peaks, dtype=int)
for i, p in enumerate(fsrii_peaks):
    if np.any(np.abs(ecg_peaks - p) <= window):
        coupled[i] = 1

# Cumulative coupling fraction
cumulative_coupling = np.cumsum(coupled) / np.arange(1, len(coupled)+1)

# Plot cumulative coupling
plt.figure(figsize=(10,4))
plt.plot(fsrii_peaks, cumulative_coupling, '-o', markersize=4)
plt.xlabel('FSRII Peak Index')
plt.ylabel('Cumulative Coupling Fraction')
plt.title('Cumulative Coupling between FSRII and ECG Peaks')
plt.ylim(0,1.05)
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Optional: Print final coupling fraction ---
print(f"Total fraction of FSRII peaks coupled with ECG: {cumulative_coupling[-1]:.2f}")

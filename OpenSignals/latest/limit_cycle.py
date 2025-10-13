import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Load CSV ---
file = r"C:\Users\diego\Github\Pythonhw\signals_GT.csv"
df = pd.read_csv(file)
fsrii = df['FSRII'].dropna().to_numpy()
ecg = df['ECG'].dropna().to_numpy()

# --- Take the same segment for both signals (optional: entire length) ---
length = min(len(fsrii), len(ecg))
fsrii_seg = fsrii[:length]
ecg_seg = ecg[:length]

# --- Normalize 0–1 ---
fsrii_norm = (fsrii_seg - np.min(fsrii_seg)) / (np.max(fsrii_seg) - np.min(fsrii_seg))
ecg_norm = (ecg_seg - np.min(ecg_seg)) / (np.max(ecg_seg) - np.min(ecg_seg))

# --- Plot ---
plt.figure(figsize=(10,5))
plt.plot(fsrii_norm, label='FSRII (normalized)')
plt.plot(ecg_norm, label='ECG (normalized)')
plt.xlabel('Sample index')
plt.ylabel('Normalized amplitude')
plt.title('Normalized FSRII and ECG')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- File paths ---
file1 = r"C:\Users\diego\Github\Pythonhw\SpO2_case2_Red_col2_IR_col1.csv"
file2 = r"C:\Users\diego\Github\Pythonhw\signals_GT.csv"

# --- Load CSVs ---
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# --- Extract data ---
spo2_1 = df1['SpO2_%'].dropna().to_numpy()
spo2_2 = df2['SpO2'].dropna().to_numpy()

# --- Smooth the first signal using a moving average ---
window_size = 10
spo2_1_smooth = np.convolve(spo2_1, np.ones(window_size)/window_size, mode='valid')

# --- Resample signals to the same length for correlation ---
min_len = min(len(spo2_1_smooth), len(spo2_2))
spo2_1_resampled = np.interp(np.linspace(0, 1, min_len), np.linspace(0, 1, len(spo2_1_smooth)), spo2_1_smooth)
spo2_2_resampled = np.interp(np.linspace(0, 1, min_len), np.linspace(0, 1, len(spo2_2)), spo2_2)

# --- Compute Pearson correlation coefficient ---
correlation = np.corrcoef(spo2_1_resampled, spo2_2_resampled)[0, 1]
print(f"Pearson correlation between signals: {correlation:.4f}")

# --- Create normalized time axes ---
t = np.linspace(0, 1, min_len)

# --- Plot both signals ---
plt.figure(figsize=(10, 5))
plt.plot(t, spo2_1_resampled, label=f'Calculated SpO2% smooth', linewidth=1.5)
plt.plot(t, spo2_2_resampled, label='Real SpO2%', linewidth=1.5)

plt.title(f'SpO₂ Comparison (Correlation = {correlation:.4f})')
plt.xlabel('Normalized Time (0 → 1)')
plt.ylabel('SpO₂ (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

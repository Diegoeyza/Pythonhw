import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
from scipy.signal import spectrogram
import re

# === File paths ===
filename_csv = r"C:\Users\diego\Documents\OpenSignals (r)evolution\files\TestClinico1.1_2025-09-22_13-49-59_2025-09-22_14-00-31_2025-09-22_14-17-06_2025-09-22_14-17-26_csv_fNIRS_metrics.csv"
filename_txt = r"C:\Users\diego\Documents\OpenSignals (r)evolution\files\Test1clinico3.txt"

# === Load CSV ===
df = pd.read_csv(filename_csv, comment="#", sep="\s+", names=["Timestamps", "HbO", "HbR"])
df["Timestamps"] = df["Timestamps"] / 100
df["SpO2"] = abs(df["HbO"] / (df["HbO"] + df["HbR"])) * 100
df["SpO2"] = df["SpO2"].clip(0, 100)
df["SpO2_smooth"] = df["SpO2"].rolling(window=25, center=True, min_periods=1).mean()

# === Read TXT header ===
with open(filename_txt, "r") as f:
    lines = f.readlines()

header_json_line = next(line for line in lines if line.startswith("# {"))
header_dict = json.loads(re.sub(r"^#\s*", "", header_json_line))

labels = header_dict["94:DE:B8:8B:92:B3"]["label"]
sensors = header_dict["94:DE:B8:8B:92:B3"]["sensor"]

channel_map = dict(zip(labels, sensors))

# === Load TXT data ===
data_start = next(i for i, line in enumerate(lines) if line.strip() == "# EndOfHeader") + 1
columns_txt = ["nSeq", "DI"] + labels
df_txt = pd.read_csv(filename_txt, sep="\s+", header=None,
                     names=columns_txt, skiprows=data_start, engine="python")

df_txt["Timestamps"] = df_txt["nSeq"] / 100
df_txt.rename(columns=channel_map, inplace=True)

# === Merge CSV and TXT ===
merge_cols = ["Timestamps"] + sensors
df = pd.merge_asof(
    df.sort_values("Timestamps"),
    df_txt[merge_cols].sort_values("Timestamps"),
    on="Timestamps",
    direction="nearest",
    tolerance=0.01
)

# === Remove duplicate columns by averaging ===
df = df.groupby(df.columns, axis=1).mean()
unique_sensors = [s for s in sensors if s in df.columns]

print(df.shape)
print(df.head())

# === TIME-DOMAIN PLOTS ===
n_plots = 2 + len(unique_sensors)
plt.figure(figsize=(14, 3 * n_plots))

# HbO & HbR
plt.subplot(n_plots, 1, 1)
plt.plot(df["Timestamps"], df["HbO"], label="HbO", color="red")
plt.plot(df["Timestamps"], df["HbR"], label="HbR", color="blue")
plt.title("HbO & HbR")
plt.grid(True)
plt.legend()

# SpO2
plt.subplot(n_plots, 1, 2)
plt.plot(df["Timestamps"], df["SpO2_smooth"], label="SpO₂ (smoothed)", color="green")
plt.title("SpO₂")
plt.grid(True)
plt.legend()

# Other sensors
for idx, sensor in enumerate(unique_sensors, start=3):
    plt.subplot(n_plots, 1, idx)
    plt.plot(df["Timestamps"], df[sensor] / 1200, label=sensor)
    plt.title(sensor)
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()

# === SPECTROGRAMS ===
plt.figure(figsize=(14, 3 * len(unique_sensors)))

for i, sensor in enumerate(unique_sensors, start=1):
    signal = df[sensor].dropna().to_numpy().astype(float)
    n = len(signal)
    if n < 4:
        print(f"Skipping {sensor}: too few samples ({n})")
        continue
    
    nperseg = min(256, n)
    nperseg = max(2, nperseg)
    noverlap = min(128, nperseg - 1)
    
    f, t, Sxx = spectrogram(signal, fs=100, nperseg=nperseg, noverlap=noverlap)
    
    plt.subplot(len(unique_sensors), 1, i)
    plt.pcolormesh(t, f, 10 * np.log10(Sxx + 1e-10), shading="gouraud", cmap="viridis")
    plt.title(f"Spectrogram - {sensor}")
    plt.ylabel("Frequency [Hz]")
    if i == len(unique_sensors):
        plt.xlabel("Time [s]")

plt.tight_layout()
plt.show()

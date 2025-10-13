import pandas as pd
import numpy as np
import json
import re
from scipy.signal import spectrogram

# === File paths ===
filename_csv = r"C:\Users\diego\Documents\OpenSignals (r)evolution\files\Test3Clinico2_2025-09-22_13-49-59_2025-09-22_14-00-31_2025-09-22_14-17-06_2025-09-22_15-04-14_csv_fNIRS_metrics.csv"
filename_txt = r"C:\Users\diego\Documents\OpenSignals (r)evolution\files\PCR2-09-22_14-51-23.txt"
file_terminator = "_GT"

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

# === SAVE REGULAR SIGNALS CSV ===
output_signals = f"signals{file_terminator}.csv"
df.to_csv(output_signals, index=False)
print(f"✅ Regular signals saved to '{output_signals}'")

# === COMPUTE & SAVE SPECTROGRAM DATA ===
spec_rows = []

for sensor in unique_sensors:
    signal = df[sensor].dropna().to_numpy().astype(float)
    n = len(signal)
    if n < 4:
        continue
    nperseg = min(256, n)
    nperseg = max(2, nperseg)
    noverlap = min(128, nperseg - 1)
    f, t, Sxx = spectrogram(signal, fs=100, nperseg=nperseg, noverlap=noverlap)
    power_db = 10 * np.log10(Sxx + 1e-10)

    # Flatten and store
    sensor_data = pd.DataFrame({
        "Sensor": sensor,
        "Time": np.repeat(t, len(f)),
        "Frequency": np.tile(f, len(t)),
        "Power_dB": power_db.flatten()
    })
    spec_rows.append(sensor_data)

df_spec = pd.concat(spec_rows, ignore_index=True)

output_spec = f"spectrogram{file_terminator}.csv"
df_spec.to_csv(output_spec, index=False)
print(f"✅ Spectrogram data saved to '{output_spec}'")

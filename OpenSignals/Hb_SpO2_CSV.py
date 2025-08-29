import pandas as pd
import matplotlib.pyplot as plt


use_time_range=True    #defines a time range if set to true
start_time=60
end_time=105


# === Load fNIRS CSV ===
filename_csv = r"C:\Users\diego\Documents\OpenSignals (r)evolution\files\OpenSignals (r)evolution Report_2025-08-29_09-12-28_csv_fNIRS_metrics_Vandro1.csv"
df = pd.read_csv(filename_csv, comment="#", sep="\s+", names=["Timestamps", "HbO", "HbR"])

# Compute SpO2
df["SpO2"] = abs(df["HbO"] / (df["HbO"] + df["HbR"])) * 100
df["Timestamps"]=df["Timestamps"]/100
df["SpO2"] = df["SpO2"].clip(0, 100)
df["SpO2_smooth"] = df["SpO2"].rolling(window=25, center=True, min_periods=1).mean()

# === Load OpenSignals TXT file ===
filename_txt = r"C:\Users\diego\Documents\OpenSignals (r)evolution\files\Test_FNIRS_Vandro_RCP1.txt"

with open(filename_txt, "r") as f:
    lines = f.readlines()

data_start = next(i for i, line in enumerate(lines) if line.strip() == "# EndOfHeader") + 1
columns_txt = ["nSeq", "DI", "CH1", "CH9A", "CH9B", "Hb"]

df_txt = pd.read_csv(
    filename_txt,
    sep="\s+",
    header=None,
    names=columns_txt,
    skiprows=data_start,
    engine="python"
)

# Add Timestamps column to txt df
df_txt["Timestamps"] = df_txt["nSeq"] /100 # adjust for sampling rate

print(df_txt.head())

# Merge CSV and TXT on nearest timestamp
df = pd.merge_asof(
    df.sort_values("Timestamps"),
    df_txt[["Timestamps", "CH1"]].sort_values("Timestamps"),
    on="Timestamps",
    direction="nearest",
    tolerance=0.01
)

if use_time_range:
    # === Define time window (in seconds) ===
    time_range = (start_time, end_time)  # <-- change this to the window you want
    df = df[(df["Timestamps"] >= time_range[0]) & (df["Timestamps"] <= time_range[1])]


# === Plotting ===
plt.figure(figsize=(12, 8))

# HbO & HbR
plt.subplot(3,1,1)
plt.plot(df["Timestamps"], df["HbO"], label="HbO", color="red")
plt.plot(df["Timestamps"], df["HbR"], label="HbR", color="blue")
plt.title("HbO & HbR")
plt.grid(True)
plt.legend()

# SpO2
plt.subplot(3,1,2)
plt.plot(df["Timestamps"], df["SpO2_smooth"], label="SpO₂", color="green")
plt.title("SpO₂ (smoothed)")
plt.grid(True)
plt.legend()

# CH1
plt.subplot(3,1,3)
plt.plot(df["Timestamps"], df["CH1"], label="CH1 Force Sensor", color="purple")
plt.title("Force Sensor (CH1)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

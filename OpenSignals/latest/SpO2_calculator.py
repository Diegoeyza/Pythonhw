#COMPARES THE CALCULATED SPO2 AND THE REAL SPO2 WITH PEARSON AND PLOTS THEM TOGETHER

import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt

# === PARAMETERS ===
filename = r"C:\Users\diego\Github\Pythonhw\signals_GT.csv"
fs = 100  # Hz (adjust if different)
win_duration = 0.5  # seconds per analysis window
cutoff_hz = 15  # Hz low-pass

# === LOAD CSV ===
df = pd.read_csv(filename)
col1, col2 = df.columns[-2], df.columns[-1]   # last 2 columns = hSpO2 signals
sig1 = df[col1].to_numpy()
sig2 = df[col2].to_numpy()

# === FILTER ===
b, a = butter(6, cutoff_hz / (fs / 2), btype="low")
sig1_f = filtfilt(b, a, sig1)
sig2_f = filtfilt(b, a, sig2)

# === FUNCTION TO COMPUTE SpO2 ===
def compute_spo2(red, ir, fs, win_duration):
    win_size = int(fs * win_duration)
    steps = range(0, len(red) - win_size, win_size)
    R_vals, SpO2_vals = [], []

    for i in steps:
        red_seg = red[i:i + win_size]
        ir_seg = ir[i:i + win_size]
        if len(red_seg) < 4: continue

        Vpp_R = np.max(red_seg) - np.min(red_seg)
        Vpp_IR = np.max(ir_seg) - np.min(ir_seg)
        Vavg_R = np.mean(red_seg)
        Vavg_IR = np.mean(ir_seg)

        if Vpp_IR == 0 or Vavg_IR == 0:
            continue

        R = (Vpp_R / Vavg_R) / (Vpp_IR / Vavg_IR)
        SpO2 = 110 - 25 * R
        R_vals.append(R)
        SpO2_vals.append(SpO2)

    df_out = pd.DataFrame({
        "WindowIndex": range(len(SpO2_vals)),
        "R": R_vals,
        "SpO2_%": SpO2_vals
    })
    # Normalize to start at 95% baseline
    if len(df_out) > 0:
        df_out["SpO2_%"] = df_out["SpO2_%"] - df_out["SpO2_%"].iloc[0] + 95
    return df_out

# === CASE 1: col1 = Red, col2 = IR ===
spo2_case1 = compute_spo2(sig1_f, sig2_f, fs, win_duration)
spo2_case1.to_csv("SpO2_case1_Red_col1_IR_col2.csv", index=False)
print(f"Saved Case 1 (Red={col1}, IR={col2}) to 'SpO2_case1_Red_col1_IR_col2.csv'")

# === CASE 2: col1 = IR, col2 = Red ===
spo2_case2 = compute_spo2(sig2_f, sig1_f, fs, win_duration)
spo2_case2.to_csv("SpO2_case2_Red_col2_IR_col1.csv", index=False)
print(f"Saved Case 2 (Red={col2}, IR={col1}) to 'SpO2_case2_Red_col2_IR_col1.csv'")

# Optional: print summaries
print("\nCase 1 mean SpO2:", np.mean(spo2_case1["SpO2_%"]))
print("Case 2 mean SpO2:", np.mean(spo2_case2["SpO2_%"]))

import pandas as pd
import numpy as np
import json
import re
from scipy.signal import spectrogram
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# === File paths ===
filename_csv = r"C:\Users\diego\Documents\OpenSignals (r)evolution\files\OpenSignals (r)evolution Report_2025-08-29_09-12-28_csv_fNIRS_metrics_Vandro1.csv"
filename_txt = r"C:\Users\diego\Documents\OpenSignals (r)evolution\files\Test_FNIRS_Vandro_RCP1.txt"
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

# === TIME-DOMAIN PLOTS (Plotly) ===
n_plots = 2 + len(unique_sensors)
fig_time = make_subplots(rows=n_plots, cols=1, shared_xaxes=True, vertical_spacing=0.02)

# HbO & HbR
fig_time.add_trace(go.Scatter(x=df["Timestamps"], y=df["HbO"], mode="lines", name="HbO", line=dict(color="red")), row=1, col=1)
fig_time.add_trace(go.Scatter(x=df["Timestamps"], y=df["HbR"], mode="lines", name="HbR", line=dict(color="blue")), row=1, col=1)

# SpO2
fig_time.add_trace(go.Scatter(x=df["Timestamps"], y=df["SpO2_smooth"], mode="lines", name="SpO2 (smoothed)", line=dict(color="green")), row=2, col=1)

# Other sensors
for idx, sensor in enumerate(unique_sensors, start=3):
    fig_time.add_trace(go.Scatter(x=df["Timestamps"], y=df[sensor] / 1200, mode="lines", name=sensor), row=idx, col=1)

# Add vertical left-side labels
subplot_labels = ["HbO / HbR", "SpO2 (smoothed)"] + unique_sensors
for i, label in enumerate(subplot_labels, start=1):
    fig_time.add_annotation(
        text=label,
        xref="paper",
        yref="y"+str(i),
        x=-0.04, y=0.5,
        xanchor="right",
        yanchor="middle",
        textangle=-90,   # Vertical text
        showarrow=False,
        font=dict(size=12)
    )

fig_time.update_layout(height=300*n_plots, width=1200, title_text="Time-Domain Signals", showlegend=True)

# Save with file terminator
fig_time.write_html(f"time_domain_plots{file_terminator}.html")
print(f"Time-domain plots saved to 'time_domain_plots{file_terminator}.html'")

# === SPECTROGRAMS (Plotly) ===
fig_spec = make_subplots(rows=len(unique_sensors), cols=1, shared_xaxes=True, vertical_spacing=0.02)

for i, sensor in enumerate(unique_sensors, start=1):
    signal = df[sensor].dropna().to_numpy().astype(float)
    n = len(signal)
    if n < 4:
        continue
    nperseg = min(256, n)
    nperseg = max(2, nperseg)
    noverlap = min(128, nperseg - 1)
    f, t, Sxx = spectrogram(signal, fs=100, nperseg=nperseg, noverlap=noverlap)

    fig_spec.add_trace(
        go.Heatmap(
            z=10 * np.log10(Sxx + 1e-10),
            x=t,
            y=f,
            colorscale="Viridis",
            colorbar=dict(title="dB")
        ),
        row=i, col=1
    )

# Add vertical left-side labels for spectrograms
for i, sensor in enumerate(unique_sensors, start=1):
    fig_spec.add_annotation(
        text=sensor,
        xref="paper",
        yref="y"+str(i),
        x=-0.03, y=0.5,
        xanchor="right",
        yanchor="middle",
        textangle=-90,   # Vertical text
        showarrow=False,
        font=dict(size=12)
    )

fig_spec.update_layout(height=300*len(unique_sensors), width=1200, title_text="Spectrograms", showlegend=False)

# Save with file terminator
fig_spec.write_html(f"spectrograms{file_terminator}.html")
print(f"Spectrograms saved to 'spectrograms{file_terminator}.html'")
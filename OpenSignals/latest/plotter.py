import pandas as pd
import matplotlib.pyplot as plt

# === Load your previously saved CSVs ===
spo2_case1 = pd.read_csv("SpO2_case1_Red_col1_IR_col2.csv")
spo2_case2 = pd.read_csv("SpO2_case2_Red_col2_IR_col1.csv")

# === Create figure ===
plt.figure(figsize=(10, 5))

plt.plot(spo2_case1["WindowIndex"], spo2_case1["SpO2_%"],
         label="Case 1 (Red = col1, IR = col2)", color="red", linewidth=2)

# plt.plot(spo2_case2["WindowIndex"], spo2_case2["SpO2_%"],
#          label="Case 2 (Red = col2, IR = col1)", color="blue", linewidth=2, linestyle="--")

# === Add labels and styling ===
plt.title("Estimated Blood Oxygenation (SpO₂) for Both Channel Assignments")
plt.xlabel("Window Index (approx. cardiac cycles)")
plt.ylabel("SpO₂ (%)")
plt.ylim(70, 105)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()

# === Show plot ===
plt.show()

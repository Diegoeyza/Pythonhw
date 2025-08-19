import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# ==============================
# 1. Load OpenSignals TXT
# ==============================
def load_opensignals_txt(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()

    # Find where the header ends
    for i, line in enumerate(lines):
        if line.strip() == "# EndOfHeader":
            start_idx = i + 1
            break

    # Load the data into a dataframe
    df = pd.read_csv(filepath, 
                     sep="\t", 
                     skiprows=start_idx, 
                     names=["nSeq", "DI", "Red", "IR"])
    return df


# ==============================
# 2. Beer-Lambert Transformation
# ==============================
def compute_hbo_hbr(df, dpf=6.0, L=3.0):
    """
    dpf = Differential Pathlength Factor (approx)
    L   = Source-detector distance in cm (approx)
    """

    # Convert raw values to optical density
    I0_red, I0_ir = df["Red"].iloc[0], df["IR"].iloc[0]
    od_red = -np.log(df["Red"] / I0_red)
    od_ir  = -np.log(df["IR"]  / I0_ir)

    # Extinction coefficients (approx, cm^-1 mM^-1)
    # [HbO, HbR]
    e_red = [0.1, 0.25]   # 660 nm
    e_ir  = [0.2, 0.05]   # 940 nm

    # Create matrix for MBLL
    E = np.array([[e_red[0], e_red[1]],
                  [e_ir[0],  e_ir[1]]])
    E_inv = np.linalg.pinv(E)  # Pseudo-inverse

    # ΔOD vector
    delta_OD = np.vstack((od_red, od_ir)).T

    # Compute concentrations (ΔC = E^-1 * ΔOD / (L * DPF))
    conc = delta_OD @ E_inv.T / (L * dpf)

    HbO = conc[:,0]
    HbR = conc[:,1]

    df["HbO"] = HbO
    df["HbR"] = HbR
    return df


# ==============================
# 3. Compute SpO2
# ==============================
def compute_spo2(df):
    df["SpO2"] = 100 * df["HbO"] / (df["HbO"] + df["HbR"] + 1e-8)
    return df


# ==============================
# 4. Save Results
# ==============================
def save_results(df, outpath="processed_signals.csv"):
    df.to_csv(outpath, index=False)
    print(f"✅ Saved results to {outpath}")


# ==============================
# 5. Plot Results
# ==============================
def plot_signals(df, start=0, end=1000):
    plt.figure(figsize=(12,6))

    plt.subplot(3,1,1)
    plt.plot(df["HbO"][start:end], label="HbO")
    plt.plot(df["HbR"][start:end], label="HbR")
    plt.legend()
    plt.ylabel("Concentration (a.u.)")
    plt.title("HbO / HbR")

    plt.subplot(3,1,2)
    plt.plot(df["SpO2"][start:end], color="green")
    plt.ylabel("SpO₂ (%)")
    plt.title("Estimated SpO₂")

    plt.subplot(3,1,3)
    plt.plot(df["Red"][start:end], label="Raw Red")
    plt.plot(df["IR"][start:end], label="Raw IR")
    plt.legend()
    plt.ylabel("Raw signal")

    plt.tight_layout()
    plt.show()


# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    file = "example_opensignals.txt"  # <- your raw file
    df = load_opensignals_txt(file)
    df = compute_hbo_hbr(df)
    df = compute_spo2(df)
    save_results(df, "processed_signals.csv")
    plot_signals(df, start=0, end=500)

import numpy as np
import matplotlib.pyplot as plt


muCox = 0.08737  # μCox en A/V^2
Vth = 2.2  # Voltaje umbral en V
W_L = 1  # Relación W/L (si no se especifica, asumimos 1)
Vds = np.linspace(0, 10, 100)  # Valores de Vds (0 a 5 V)
Vgs_values = [2.5, 3, 3.5, 4.0, 4.5, 5, 5.5, 6, 6.5]  # Valores de Vgs

plt.figure(figsize=(10, 6))
for Vgs in Vgs_values:
    Id = []
    for vds in Vds:
        if vds < (Vgs - Vth):  # Régimen lineal
            id_value = muCox * W_L * ((Vgs - Vth) * vds - (vds**2) / 2)
        else:  # Régimen de saturación
            id_value = 0.5 * muCox * W_L * (Vgs - Vth)**2
        Id.append(id_value)
    plt.plot(Vds, Id, label=f"Vgs = {Vgs} V")

plt.xlabel("Vds (V)")
plt.ylabel("Ids (A)")
plt.title("Curves calculated with the ecuation")
plt.grid(True)
plt.legend()
plt.show()
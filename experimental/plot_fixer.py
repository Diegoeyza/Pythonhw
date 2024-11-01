import pandas as pd
import matplotlib.pyplot as plt
if (False):
    # Cargar el archivo .txt en un DataFrame
    archivo = r"C:\Users\diego\AppData\Local\Microsoft\Windows\INetCache\IE\90KEM0ES\F0001CH1[1].CSV"
    data = pd.read_csv(archivo, delimiter=',', skiprows=1, usecols=[1, 3], names=['time', 'voltage'])

    # Convertir las columnas a valores numéricos (limpiando cualquier espacio en blanco adicional)
    data['time'] = pd.to_numeric(data['time'], errors='coerce')
    data['voltage'] = pd.to_numeric(data['voltage'], errors='coerce')

    # Asignar tiempo secuencial si es necesario, o usar el tiempo original
    if data['time'].isna().all():  # Solo si 'time' no tiene datos válidos, asignamos secuencialmente
        data['time'] = range(len(data))

    # Graficar tiempo vs. voltaje
    plt.plot(data['time'], data['voltage'], label="Voltaje")
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.title("Gráfico de Tiempo vs Voltaje")
    plt.legend()
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo, saltando la cabecera de metadatos
archivo = r"C:\Users\diego\AppData\Local\Microsoft\Windows\INetCache\IE\90KEM0ES\F0001CH1[2].CSV"

# Leer el archivo completo primero para encontrar dónde comienzan los datos reales
with open(archivo, 'r') as file:
    lines = file.readlines()

# Encontrar la primera fila de datos
data_start = None
for i, line in enumerate(lines):
    # Asumiendo que los datos comienzan con una línea con tres comas consecutivas y luego los valores de tiempo y voltaje
    if line.count(',') >= 3 and all(item.strip() for item in line.split(',')[3:5]):
        data_start = i
        break

# Si no encontramos datos, lanzamos un error
if data_start is None:
    raise ValueError("No se encontró la sección de datos en el archivo.")

# Cargar solo las filas de datos
data = pd.read_csv(archivo, delimiter=',', skiprows=data_start, usecols=[3, 4], names=['time', 'voltage'])

# Convertir los datos a valores numéricos
data['time'] = pd.to_numeric(data['time'], errors='coerce')
data['voltage'] = pd.to_numeric(data['voltage'], errors='coerce')

# Graficar tiempo vs. voltaje
plt.plot(data['time'], data['voltage'], label="Voltaje")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.title("Gráfico de Tiempo vs Voltaje")
plt.legend()
plt.show()

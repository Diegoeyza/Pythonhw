import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo .txt en un DataFrame
archivo = 'Lab1_V2.txt'
data = pd.read_csv(archivo, delimiter='\t', skiprows=1, names=['Voltaje', 'Corriente'])

# Valores específicos de voltaje y corriente para la recta de carga
V_max = float(input("Ingrese voltaje(V):"))
I_max = 0.02

pos = 0
for i in range(0, len(data['Corriente']+1)):
  if i > 10:
    if abs(data['Corriente'][i] - I_max) < abs(data['Corriente'][pos] - I_max) :
      pos = i
I_L = data['Corriente'][pos]
Vol_L = data['Voltaje'][pos]


p=I_max/(2.17-3.1875)
c=V_max*p*(-1)
def f_carga(x):
  y=(c+p*float(x))*1000
  return y
r_carga=[]
for i in range(0,len(data['Voltaje']+1)):
  r_carga.append(f_carga(data['Voltaje'][i]))

for i in range(len(r_carga)):
  print(r_carga[i],i )
Resis = (V_max/c)
x1 = []
n = V_max/10

# Graficar los datos y la recta de carga
plt.plot(data['Voltaje'], r_carga, "r", label = 'Recta de carga')
plt.plot(data['Voltaje'], data['Corriente'], label='Datos')
#plt.plot(x1, f_carga(x1), label='Recta de carga', linestyle='--')
# Configurar la gráfica
plt.scatter( 2.17, 20, color="green")
plt.xlabel('Voltaje (V)')
plt.ylabel('Corriente (mA)')
plt.title('Gráfico de Datos y Recta de Carga')
plt.legend()
plt.grid(True)
plt.show()

print("La resistencia es: ", Resis)
print(V_max, Vol_L, I_L)
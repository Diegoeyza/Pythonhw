from multiprocessing.dummy import Array
import numpy as np
from numpy import *
from scipy.linalg import *

print("Parte 1\n")
B=matrix([[1,0,0,0,0,0,0,0,0,1],[0,1,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,1,0,0],[0,0,0,1,0,0,1,0,0,0],[0,0,0,0,-1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,0,-1,0,0,0],[0,0,1,0,0,0,0,-1,0,0],[0,-1,0,0,0,0,0,0,1,0],[1,0,0,0,0,0,0,0,0,-1]])
ortonormal=0
for i in range (0, len(B)):
    a=np.array(B.T[i])
    c=0
    if linalg.norm(a)==1:       #uso linalg.norm porque es la forma más optimizada, pero la manera teórica de hacerlo sería: if np.dot(a,a.T)==1:    no hace falta sacar la raíz en este caso dado que la normal debe ser 1 y raíz de 1 es 1
        for j in range (0, len(B)):
            b=np.array(B.T[j])
            c=c+abs(np.dot(a,b.T)[0,0])
        if c!=1:
            ortonormal=1
    else:
        ortonormal=1
if ortonormal==0:
        print(f"La base en cuestión (cada columna es un vector): \n {B}\n")
        print("La base mostrada es ortonormal\n")

else:
    print(f"La base en cuestión (cada columna es un vector): \n {B}\n")
    print("La base mostrada no es ortonormal\n")

print("parte 2\n")
p=np.poly1d(np.array([7,-6,5,-4,3,-2,1,0]).astype(np.float64)) #defino el polinomio como un array tipo float dado que numpy tiene problemas al trabajar resta de polinomios de grados altos y al trabajar con floats se soluciona
print(f"El grado del polinomio es {p.order}\n")
print(f"Las raices de p son:  {p.r}\n")
for i in range (-53, 52): #NOTA:EL PROFESOR NOS COMENTÓ QUE EL -73 EN LA TAREA SE REFERÍA A UN -53, PORQUE SI NO EL PATRÓN NO HACE SENTIDO
    print(f"El resultado de P({i})={p(i)}")
print("\nFin del spam\n")
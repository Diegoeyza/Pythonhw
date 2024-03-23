import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#I
print("pregunta 1, I:")
def EDO(u,t):
    dudt= 500+np.exp(-t/2)-0.5*u #dejo toda la funcion al lado derecho así dejando u´ al lado izquierdo
    return dudt
u0=0
x= np.arange(0.0,600.0,0.1)
#ya teniendo armado el PVI, le doy los valores a R correspondientes
sol=odeint(EDO,u0,x)
print(f"la posición aproximada del nadador sería\n{sol[-1]}\nLa cual es aproximable a 1 kilometro")
print("pregunta 1, II:")

h=0.5
N = int(L/h)   
Xp = np.zeros(N+1)
Yp = np.zeros(N+1)
t0=0.0
tf=600.0
Xp[0] = x0
Yp[0] = y0
L = tf-t0
h = L/N
for n in range(N):
    if n==0:
        f = np.exp(-x0)*y0-np.cos(x0**2)
        y = y0 + h*f
        x = x0 + h
        Xp[n+1] = x
        Yp[n+1] = y
    else:
        f = np.exp(-x)*y-np.cos(x**2)
        y = y + h*f
        x = x + h
        Xp[n+1] = x
        Yp[n+1] = y
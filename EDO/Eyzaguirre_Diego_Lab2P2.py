import numpy as np
from scipy.integrate import odeint, solve_bvp
import matplotlib.pyplot as plt
def ER(lista1, lista2, lista3):
    E1=abs((lista1[len(lista1)-1]-lista3[len(lista3)-1])*100/lista3[len(lista3)-1])
    E2=abs((lista2[len(lista2)-1]-lista3[len(lista3)-1])*100/lista3[len(lista3)-1])
    if E1<E2:
        E=[E1,E2]
        print ("Euler progresivo tiene menor error")
        return E
    elif E1<E2:
        E=[E2,E1]
        print ("Euler retrógrado tiene menor error")
        return E
def GER(lista1, lista2, lista3):            #grafico el error de manera distinta a la guía, dado que prefiero el sistema de error clásico (término a término)
    Ep = np.zeros(len(lista3)-1)
    Er = np.zeros(len(lista3)-1)
    for i in range (0, len(lista3)-1):
        E1=abs((lista1[i]-lista3[i])*100/lista3[i])
        E2=abs((lista2[i]-lista3[i])*100/lista3[i])
        Ep[i]=E1
        Er[i]=E2
    return Ep,Er

x0 = 0.0
xf = 1.99
y0 = 1.0
L = xf-x0
h = 0.01
N = int(L/h)
Xp = np.zeros(N+1)
Yp = np.zeros(N+1)
Xp[0] = x0
Yp[0] = y0
def EDO(y, x):
    dxdy= 3*y+x
    return float(dxdy)
xi= np.arange(0.0,2,0.01)
s=odeint(EDO,y0,xi)
for n in range(N):
    if n==0:
        f = 3*y0+x0
        y = y0 + h*f
        x = x0 + h
        Xp[n+1] = x
        Yp[n+1] = y
    else:
        f = 3*y+x
        y = y + h*f
        x = x + h
        Xp[n+1] = x
        Yp[n+1] = y

Xr = np.zeros(N+1)
Yr = np.zeros(N+1)
Xr[0] = x0
Yr[0] = y0
for n in range(N):
    if n==0:
        x = x0 + h
        y = (h*x + y0)/(1 - 3*h)           #despejo a y en la ecuación y me queda de esta forma 
        Xr[n+1] = x
        Yr[n+1] = y
    else:
        x = x + h
        y = (h*x + y)/(1 - 3*h)
        Xr[n+1] = x
        Yr[n+1] = y
plt.plot(Xp,Yp,label="Progresivo",color="blue")
plt.plot(Xr,Yr,label="Retrógrado",color="green")
plt.plot(xi,s,label="Solucion",color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
Ep,Er=GER(Yp,Yr,s)
plt.plot(Xp[0:199],Ep,label="Error Progresivo",color="blue")
plt.plot(Xr[0:199],Er,label="Error Retrógrado",color="green")
plt.xlabel("x")
plt.ylabel("error porcentual")
plt.legend()
plt.show()
print("como se puede ver, su error es prácticamente igual y crece, por lo que lo vemos con una función para ver cual tiene menor error (aunque ya se avista que el progresivo tiene menor)")
E=ER(Yp,Yr,s)
print(f"Su error es de {E[0]}% comparado con el otro que es de {E[1]}%")
#acorde al error, euler progresivo se mantiene más cercano al caso real de la EDO a medida que se crece en x. esto es probablemente debido a que, como euler progresivo se utiliza aproximación por el rectángulo inferior, y queda más cerca gracias a que no excede a la función, la cual tiene pendiente similar a la exponencial, por lo que si aproximamos por triángulo superior (euler retrógrado), nos va a dar valores aproximados cada vez mayores
#el comentario se agregó, dado que, al utilizar euler retrógrado, se utiliza la siguiente iteración para la obtención implícita de la misma, pero si se intentara realizar esta iteración al límite del dominio, no sería posible obtenerla, dado que el x sub n+1 no existe pues se sale del dominio
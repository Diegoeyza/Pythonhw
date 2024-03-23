import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
value=int(input("seleccione 1 si quiere el gráfico con h=0,5 o seleccione 2 si lo quiere con h=0,05: "))
x0 = 0.0
xf = 10.0
y0 = 1.0
L = xf-x0
def EDO(y, x):
    dxdy= np.exp(-x)*y-np.cos(x**2) 
    return float(dxdy)



if value==1:
    xi= np.arange(0.0,10.0,0.5)     #lo dejo en 0.5 para que la sol de la EDO sea concordante con el h en este caso
    s=odeint(EDO,y0,xi)
    h=0.5
    N = int(L/h)   
    Xp = np.zeros(N+1)
    Yp = np.zeros(N+1)
    Xp[0] = x0
    Yp[0] = y0
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

    Xm = np.zeros(N+1)
    Ym = np.zeros(N+1)
    Xm[0] = x0
    Ym[0] = y0
    for n in range(N):
        if n==0:
            y = y0 + h*(np.exp(-(x0+h/2))*(y0+h*(np.exp(-x0)*y0-np.cos(x0**2))/2)-np.cos((x0+h/2)**2))      #esta es la expresión de y sub n+1 de euler modificado una vez despejo el y tongo y el x tongo en función de x0 e y0, lo mismo se hace más adelante para x e y solos
            x = x0 + h
            Xm[n+1] = x
            Ym[n+1] = y
        else:
            y = y + h*(np.exp(-(x+h/2))*(y+h*(np.exp(-x)*y0-np.cos(x**2))/2)-np.cos((x+h/2)**2))
            x = x + h
            Xm[n+1] = x
            Ym[n+1] = y

    plt.plot(Xp,Yp,label="Progresivo",color="blue")
    plt.plot(Xm,Ym,label="Modificado",color="green")
    plt.plot(xi,s,label="Solucion",color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

elif value==2:
    xi= np.arange(0.0,10.0,0.05)        #lo dejo en 0.05 para que la sol de la EDO sea concordante con el h en este caso
    s=odeint(EDO,y0,xi)
    h=0.05
    N=int(L/h)
    Xp = np.zeros(N+1)
    Yp = np.zeros(N+1)
    Xp[0] = x0
    Yp[0] = y0
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

    Xm = np.zeros(N+1)
    Ym = np.zeros(N+1)
    Xm[0] = x0
    Ym[0] = y0
    for n in range(N):
        if n==0:
            f = np.exp(-x0)*y0-np.cos(x0**2)
            y = y0 + h*(np.exp(-(x0+h/2))*(y0+h*(np.exp(-x0)*y0-np.cos(x0**2))/2)-np.cos((x0+h/2)**2))
            x = x0 + h
            Xm[n+1] = x
            Ym[n+1] = y
        else:
            f = np.exp(-x)*y-np.cos(x**2)
            y = y + h*(np.exp(-(x+h/2))*(y+h*(np.exp(-x)*y-np.cos(x**2))/2)-np.cos((x+h/2)**2))
            x = x + h
            Xm[n+1] = x
            Ym[n+1] = y

    plt.plot(Xp,Yp,label="Progresivo",color="blue")
    plt.plot(Xm,Ym,label="Modificado",color="green")
    plt.plot(xi,s,label="Solucion",color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
else:
    print("no ha ingresado un valor compatible")

#pareciera ser que euler modificado aproxima mejor la solución, dado que al comienzo de la gráfica de h=0.5, euler modificado era más parecido que euler retrógrado, aunque luego de superar el x=5 ambas se alejan de la solución. y pareciera ser que a menor h, más parecidos son los métodos de euler a la solución, como se ve con h=0.05, por ende, el cambio al usar h es que hace la gráfica más precisa y suave que usar un h mayor 
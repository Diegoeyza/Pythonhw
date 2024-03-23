import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def EDO(i,x,R):
    didt= 5*(12-R*i) #dejo toda la funcion al lado derecho así dejando di/dt al lado izquierdo
    return didt
i1,i2,i3=1,1,1
i0=0
print("pregunta 2:")
x= np.arange(0.0,10.0,0.1)
#ya teniendo armado el PVI, le doy los valores a R correspondientes
R=4
i1=odeint(EDO,i0,x,args=(R,))
R=20
i2=odeint(EDO,i0,x,args=(R,))
R=0.2
i3=odeint(EDO,i0,x,args=(R,))
plt.plot(x,i1,label="R=4",color="blue")
plt.plot(x,i2,label="R=20",color="green")
plt.plot(x,i3,label="R=0.2",color="red")
plt.xlabel("t")
plt.ylabel("i(t)")
plt.legend()
plt.show()
#del gráfico se deduce que a menor resistencia, mayor voltaje (i) va a resultar del circuito, por ende, se produce menor pérdida de energía en forma de calor con 0,2 de resistencia comparado con 4 de resistencia, que reduce el voltaje a alrededor de 1/20 del de 0,2 (notandose más el efecto a medida que aumenta el t, aunque se comienza a estabilizar en t=4). también se puede ver que el tiempo de estabilización de la corriente se reduce a medida que crece la resistencia.
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


num=int(input("Presione 1 si desea ver la parte 1, 2, 3 o 4 para ver la parte correspondiente, o 0 para terminar: "))
while num!=0:
#parte 1
    V1=np.array([1,2,3])
    V2=np.array([1,-1,0])
    V3=np.array([1,1,0])
    t=np.arange(-10,10,0.1)
    if num==1:
        D1=V2-V1
        X1=V1[0]+t*D1[0]
        Y1=V1[1]+t*D1[1]
        Z1=V1[2]+t*D1[2]
        fig1=plt.figure()
        ax1=Axes3D(fig1)
        ax1.plot3D(X1,Y1,Z1)
        plt.show()

#parte 2
    elif num==2:
        D2=V3-V1
        X2=V1[0]+t*D2[0]
        Y2=V1[1]+t*D2[1]
        Z2=V1[2]+t*D2[2]
        fig2=plt.figure()
        ax2=Axes3D(fig2)
        ax2.plot3D(X2,Y2,Z2)
        plt.show()

#parte 3
#ecuación del plano echa a mano: 3X+3Y-3Z=0, se puede hacer con python con np.cross(V1, V2) para obtener el vector normal del plano y luego resolverlo para obtener la Z en relación a X e Y, pero como el comando no fue mencionado, decidí hacerlo a mano (lo mismo en la 4)
    elif num==3:
        X = np.arange(-2, 2, 0.1)
        Y = np.arange(-2, 2, 0.1)
        X, Y = np.meshgrid(X, Y)
        Z = X+Y     #relación entre el Z con respecto al X e Y de la ecuación cartesiana del plano (3X-3+3Y-6-3Z+9=0)
        fig = plt.figure()
        ax = Axes3D(fig)
        surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='bone')
        plt.show()

#parte 4
#ecuación del plano es: X-Y
    elif num==4:
        n=-(1000000000000^10000000000)
        while n<1000000000000^10000000000:
            X = np.arange(-2, 2, 0.1)
            Y = np.arange(-2, 2, 0.1)
            X, Y = np.meshgrid(X, Y)
            Z = n           
            fig = plt.figure()
            ax = Axes3D(fig)
            surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='bone')
            plt.show()
            n=n+1
    else: 
        print ("Comando distinto a los mencionados, reiniciando programa...\n")
    num=int(input("Presione 1 si desea ver la parte 1, 2, 3 o 4 para ver la parte correspondiente, o 0 para terminar: "))
print ("Gracias por su tiempo :)")
import numpy as np
def transpuesta(matriz):
    if np.array_equal(matriz, matriz.T)==True:
        return(print(f"La matriz \n{matriz}\n es simétrica\n"))
    else:
        return(print(f"La matriz \n{matriz}\n no es simétrica\n"))

respuesta=int(input("Si desea ver ambas respuestas presione 0, si desea ver la respuesta 1, presione 1, si desea ver la respuesta 2, presione 2: "))
if respuesta==1:
    print("\nPregunta 1\n")
    A=np.matrix([[1,2,3,4,5],[1,-1,1,-1,1],[3,3,3,3,3],[5,4,3,2,1],[6,7,8,9,10]])
    B=np.matrix([[1,2,3,4,5],[2,1,2,1,2],[3,2,3,2,3],[4,1,2,1,4],[5,2,3,4,2]])
    C=np.matrix([[0,2,3,4,5],[-2,0,2,1,2],[-3,-2,0,2,3],[-4,-1,-2,0,4],[-5,-2,-3,-4,0]])
    D=np.matrix([[0,2,1,6],[0,0,1,2],[0,0,0,3],[0,0,0,0]])
    E=np.matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
    F=np.matrix([[0,1,0],[0,1,0],[0,1,0]])
    transpuesta(A)
    transpuesta(B)
    transpuesta(C)
    transpuesta(D)
    transpuesta(E)
    transpuesta(F)
elif respuesta==2:
    print("\nPregunta 2")
    A=np.matrix([[1,2,3,4,5],[1,-1,1,-1,1],[3,3,3,3,3],[5,4,3,2,1],[6,7,8,9,10]])

    print("\nParte 1")
    A1=(A**2)+A
    print(A1.diagonal())

    print("\nParte 2")
    A2=(A**3)-A
    print(A2.min())

    print("\nParte 3")
    A3=A.T+A
    print(A3.max())
elif respuesta==0:
    print("\nPregunta 1\n")
    A=np.matrix([[1,2,3,4,5],[1,-1,1,-1,1],[3,3,3,3,3],[5,4,3,2,1],[6,7,8,9,10]])
    B=np.matrix([[1,2,3,4,5],[2,1,2,1,2],[3,2,3,2,3],[4,1,2,1,4],[5,2,3,4,2]])
    C=np.matrix([[0,2,3,4,5],[-2,0,2,1,2],[-3,-2,0,2,3],[-4,-1,-2,0,4],[-5,-2,-3,-4,0]])
    D=np.matrix([[0,2,1,6],[0,0,1,2],[0,0,0,3],[0,0,0,0]])
    E=np.matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
    F=np.matrix([[0,1,0],[0,1,0],[0,1,0]])
    transpuesta(A)
    transpuesta(B)
    transpuesta(C)
    transpuesta(D)
    transpuesta(E)
    transpuesta(F)

    print("\nPregunta 2")
    A=np.matrix([[1,2,3,4,5],[1,-1,1,-1,1],[3,3,3,3,3],[5,4,3,2,1],[6,7,8,9,10]])

    print("\nParte 1")
    A1=(A**2)+A
    print(A1.diagonal())

    print("\nParte 2")
    A2=(A**3)-A
    print(A2.min())

    print("\nParte 3")
    A3=A.T+A
    print(A3.max())
else:
    print("Error, ingrese un valor de los mencionados anteriormente (0, 1 o 2)")
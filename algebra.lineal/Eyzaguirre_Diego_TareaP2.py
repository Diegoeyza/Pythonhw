from multiprocessing.dummy import Array
import numpy as np
from numpy import *
from scipy import linalg
def null(A, eps=1e-15):
    u, s, vh = linalg.svd(A)
    null_mask = (s <= eps)
    null_space = compress(null_mask, vh, axis=0)
    return transpose(null_space)
A1=np.matrix([[1,4],[4,1]])
A2=np.matrix([[1,4,0],[4,1,0],[0,0,4]])
A3=np.matrix([[2,1,1],[1,2,1],[1,1,2]])
A4=np.matrix([[2,0,0,0],[0,2,1,1],[0,1,2,1],[0,1,1,2]])
A5=np.matrix([[2,1,1,1],[1,2,1,1],[1,1,2,1],[1,1,1,2]])
matrices=[A1, A2, A3, A4, A5]

def PDP(M):
    q=linalg.eig(M)                             #busco los valores y vectores propios de la matriz entregada
    s=M.shape[0]                                #guardo la cantidad de filas para ver su tamaño (dado que es cuadrada me basta con saber sus filas)
    D=np.zeros((s, s), dtype = 'complex_')      #creo una matriz de puros ceros con parte real y compleja, dado que los valores propios que se me entregaron tienen parte compleja
    V=q[1].astype('complex_')                   #creo la matriz P, que es una matriz de todos los vectores propios como columnas
    VI=np.linalg.inv(V)                         #creo la matriz P inversa
    vp=q[0]                                     #creo una lista con los valores propios
    for i in range (0,s):
        D[i,i]=np.exp(vp[i])                    #reemplazo la diagonal de D con los valores propios correspondientes luego de convertirlos en su exponencial
    PD=np.matmul(V,D)                           #multiplico matrices (sólo se pueden multiplicar 2 a la vez, si no da mal el resultado)
    A=np.matmul(PD,VI)                          #termino de crear exp(A) por medio de su forma diagonzalizada
    return A                                    #retorno la matriz exp(A)

#a continuación printeo los resultados y calculo el resultado de exp(A) por exp(-A)
for i in range (0,5):
    print(f"La matriz exp(A{i+1}) es: \n{PDP(matrices[i])}\n")
    I=np.zeros((matrices[i].shape[0],matrices[i].shape[1] ), dtype = 'complex_')
    for j in range (0, matrices[i].shape[0]):
         I[j,j]=1
    if I.all==(np.matmul(PDP(matrices[i]), PDP((-matrices[i])))).all:               #comparo para ver si esque las matrices exp (A) y exp(-A) dan la matriz identidad o no usando .all para analizar todos los elementos
        print(f"La multiplicación de exp(A{i+1}):\n{PDP(matrices[i])}\n con exp(-A{i+1}):\n{PDP(-(matrices[i]))}\n da la matriz identidad\n")
    else: 
        print(f"La multiplicación de exp(A{i+1}):\n{PDP(matrices[i])}\n con exp(-A{i+1}):\n{PDP(-(matrices[i]))}\n no da la matriz identidad, si no que da:\n {np.matmul(PDP(matrices[i]), PDP((-matrices[i])))}\n")
#el resultado de la exp(A) con exp(-A) va a variar dependiendo de la versión de numpy, pero principalmente se consiguen matrices similares a la identidad porque python tiene problemas con calcular números enteros, dejándolos como un número decimal muy parecido a este (por ejemplo 0,00000001 en vez de 0). matemáticamente todas dan la identidad dado que, como la matriz diagonal D de una ponderada con la de la otra dan exáctamente una matriz identidad (la de una va a ser euler elevado a algo, y la otra 1/euler elevado a eso mismo), se puede deducir que la relación entre sus vectores propios es la misma, dado que para calcular los vectores propios se usan los valores propios. de esto se puede deducir que si dos matrices de la misma forma tienen matrices diagonales de sus valores propios que ponderadas entre sí dan 0, las matrices en sí son inversas entre sí.


print("Final feliz")
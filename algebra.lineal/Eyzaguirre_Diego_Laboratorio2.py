import csv
import numpy as np
from numpy import *
from scipy.linalg import *
print("Parte 1\n")
M=matrix([[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,1],[0,0,0,0,1]])
b=matrix([[3],[3],[1],[1],[2]])
print(f"Matriz inicial: \n{M}\n")
print(f"solución a encontrar: \n{b}\n")
x=solve(M,b)
print(f"solución: \n {x}\n\n")

print("parte 2\n")
File=open("O-D.csv")
ObjCSV=csv.reader(File)
Data=list(ObjCSV)
m=Data.__len__()-1
n=Data[0].__len__()-1
A=np.zeros((m,n))
for i in np.arange(1,m+1):
    for j in np.arange(1,n+1):
        A[i-1][j-1]=Data[i][j]
print(A)
File.close()
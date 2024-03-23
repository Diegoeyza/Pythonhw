from multiprocessing.dummy import Array
import numpy as np
from numpy import *
from scipy import linalg
def null(A, eps=1e-15):
    u, s, vh = linalg.svd(A)
    null_mask = (s <= eps)
    null_space = compress(null_mask, vh, axis=0)
    return transpose(null_space)

def TL(N):
    C=null(N)
    DO=N.shape[0]                                #dimensión espacio de inicio y es igual a la del espacio de llegada por el enunciado
    if C.size==0 and DO==DO:                     #uso TNI para ver epiyectividad, lo de DO==DO es sólo por hacer la formula correcta, aunque sea obvio que es true
        return print(f"La transformación:\n {N}\nEs isomorfismo (biyectiva)")
    elif C.size==0 and DO!=DO:
        return print(f"La transformación:\n {N}\n Es monomorfismo (inyectiva), pero no epimorfismo (epiyectiva) y por ende no es isomorfismo (biyectiva)")
    elif C.size!=0 and (DO-C.size)==DO:               #por TNI, la dim de la imágen es dim de el espacio de inicio menos la dim del ker, y si esto es igual a la dim del espacio de llegada la TL es epiyectiva
        return print(f"La transformación:\n {N}\n Es epimorfismo (epiyectiva), pero no monomorfismo (inyectiva) y por ende no es isomorfismo (biyectiva)")  
    else:
        return print(f"La transformación:\n {N}\n No es isomorfismo (inyectiva), ni epimorfismo (epiyectiva) y por ende no es isomorfismo (biyectiva)")  
    


A=np.matrix([[2,-3],[-6,9]])
B=np.matrix([[1,1,3],[1,3,1],[3,1,1]])
C=np.matrix([[1,1,1,1],[1,1,1,-1],[1,1,-1,-1],[1,-1,-1,-1]])
TL(A)
TL(B)
TL(C)

#comentario respondiendo a la pregunta sobre el valor propio: se puede analizar (al ojo de hecho) si esque hay filas o columnas que son LD entre sí (que operandose entre sí se puedan eliminar, columnas también dado que al buscar el determinante se pueden operar columnas), si al menos hay una que se puede eliminar, hay un valor propio que va a ser 0, dado que para calcular los valores propios se utilizan los términos de las filas como valores que multiplican.
        


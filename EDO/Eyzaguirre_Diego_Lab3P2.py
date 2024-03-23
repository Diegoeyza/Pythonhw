from sympy import Function, Eq, Derivative, shape, dsolve
from sympy.abc import t
from sympy.matrices import Matrix
from numpy import dot
print ("Pregunta a:")
EDO= "1*y2 -2*y1 +1*y"          #procedo a normalizar si esque no estuviera normalizado (ya lo está, por lo que no divido por lo que acompaña a y2)
EDO=EDO.split(" ")
a0,a1=-int(EDO[2].strip("*y").strip("+")),-int(EDO[1].strip("*y1").strip("+"))    #creo los valores necesarios para pasar la EDO a matriz
x1 = Function('x1')             #definimos a x1 como funcion
x2 = Function('x2')             #definimos a x2 como funcion
A = (Eq(Derivative(x1(t),t),x2(t)),Eq(Derivative(x2(t),t),a0*x1(t)+a1*x2(t)))
Am=Matrix([[0,1],[a0,a1]])              #dejo la matriz de forma más simple de ver por comodidad
print(f"La matriz A queda de la forma\n{Am}")
print ("\nPregunta b:")
S=dsolve(A)                           #Consigo la solución a la EDO
print(f"La solución general es\n{S}") #considerar que los - presentes pueden ignorarse dado que varían acorde a la constante
print ("\nPregunta c:")               #utilizo el segundo término de la solución, dado que va asociado a x2 y este es igual a y´ según el cambio de variable y multiplico las C por -1 para que queden más bonitas (las C pueden ser cualquier valor)
yp=str(S[1].rhs)
yp=yp.replace("- ", "+ ").replace("-", "")
print(f"y´(t) va a ser igual a:\n{yp}")

from sympy import Function, dsolve, Derivative, exp, sin, cos, checkodesol, symbols 
from sympy.abc import x
import numpy as np
import matplotlib.pyplot as plt

y = Function("y") #definimos a y como la función a resolver
x, C1 , C2 , C3 = symbols("x,C1,C2,C3")
print("pregunta 1 parte a:")
print(dsolve(Derivative(y(x),x,x,x)-6*Derivative(y(x),x,x)+12*Derivative(y(x),x)-8*y(x))) #forma homogénea de la EDO, en otras palabras todo f(x) es igual a 0, por lo que se elimina la exp(x) y el sin(x)
#análisis pregunta a: se puede ver que da las 3 soluciones esperadas, cada una LI con la otra, dándonos así toda la gama posible de las soluciones de H haciendo combinaciones entre las soluciones con los coeficientes constantes. siguiendo esta línea, podemos decir que exp(2*x) es sol si hacemos que C1=1, C2=0 y C3=0
print("parte b:")
resultado=dsolve(Derivative(y(x),x,x,x)-6*Derivative(y(x),x,x)+12*Derivative(y(x),x)-8*y(x)-sin(x)-x*exp(x)) #forma completa de la EDO
print(resultado)
print(checkodesol(Derivative(y(x),x,x,x)-6*Derivative(y(x),x,x)+12*Derivative(y(x),x)-8*y(x)-sin(x)-x*exp(x), resultado))
print("Al retornar true, podemos decir que la solución general es la solución de la EDO completa")
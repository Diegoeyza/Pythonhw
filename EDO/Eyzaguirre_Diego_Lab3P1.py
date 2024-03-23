from sympy import Function, Eq, Derivative, shape, dsolve
from sympy.abc import t
from sympy.matrices import Matrix
from numpy import dot
print ("Pregunta a:")
x1 = Function('x1') #definimos a x1 como funcion
x2 = Function('x2') #definimos a x2 como funcion
A = (Eq(Derivative(x1(t),t),5*x1(t) + 3*x2(t)),Eq(Derivative(x2(t),t),-2*x1(t)))
S=dsolve(A)
S[0]=S[0].rhs
S[1]=S[1].rhs
S[0]=str(S[0])
S[1]=str(S[1])
for i in range (0,len(S)):
    S[i]=S[i].replace("C1*", "").replace("C2*", "").replace("- ", "-").replace("+ ", "+").split(" ")
M=Matrix(S)
print (f"Mi matriz fundamental va a ser {M}")
print ("\nPregunta b:")
Mi=M**-1
vi=0                                            #valor de la condición inicial, o en otras palabras el valor que va a tomar el M-1
M0=Mi.subs(t, vi)                               #reemplazo los t de mi matriz inversa fundamental con el valor de la condición inicial
X0=Matrix([[1],[-1]])                           #creo el vector de condiciones iniciales
SH=M*M0*X0                                      #extraigo la solución homogénea por medio de la fórmula
print(f"Mi solución al PVI es {SH}")

print ("\nPregunta c: (está como comentario)")
#Teóricamente, consideremos el hecho de que cada matriz fundamental requiere de las soluciones individuales como columna, las cuales provienen de los vectores propios. siguiendo esta estructura, se puede ver que el órden de las columnas va a depender totalmente de cual valor propio se considere primero, por lo que son intercambiables. también es posible multiplicar los vectores propios sin cambiar su validez, dado que siguen siendo vectores propios siempre y cuando todos los términos del vector sean ponderados por la misma constante. Finalmente, podemos ver que la matriz fundamental dada (M0) y la que nosotros sacamos (M1) son equivalentes de la siguiente manera: cambio las columnas de M0 (cambiando el órden de los valores propios), multiplico toda la matriz M0 por -1 (equivalente a multiplicar cada vector pripio, por lo que es válido) y por último multiplico la columna de e**3t por 2 (equivalente a multiplicar este vector propio por 2). Luego de estas operaciones se puede ver que M0 y M1 son equivalentes, pero no iguales como matriz fundamental para el PVI dado
#TLDR: no son iguales pero son equivalentes porque depende del orden de los vectores propios y sus ponderadores
#otra manera de hacerlo sería por medio de la propiedad M´=MA siempre y cuando det(M) sea distinto de 0, pero preferí no hacerlo dado que el producto punto no funcionó bien


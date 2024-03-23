from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform
from sympy.abc import x, s
from sympy import Symbol, exp, cos, sin, Heaviside
command=str(input("Ingrese la pregunta deseada (a o b): "))
a=Symbol('a')
b=Symbol('b', positive=True)
if command=="a":
    fx1,fx2,fx3,fx4=sin(2*x),exp(x)*cos(3*x),x*exp(x),sin(2*x)+exp(x)*cos(3*x)-x*exp(x)
    print("Pregunta 1, a:")
    print(f"La transformada de Laplace para sin(2x) es:\n{laplace_transform(fx1,x,s,noconds=True)}\n")
    print(f"La transformada de Laplace para (e^x)cos(3x) es:\n{laplace_transform(fx2,x,s,noconds=True)}\n")
    print(f"La transformada de Laplace para x(e^x) es:\n{laplace_transform(fx3,x,s,noconds=True)}\n")
    print(f"La transformada de Laplace para sin(2x)+(e^x)cos(3x)-x(e^x) es:\n{laplace_transform(fx4,x,s,noconds=True)}")
elif command=="b":
    fs1,fs2,fs3=-1/(2*(s+2)**2)+1/(2*(s-2)**2),s*exp(-s)/((s**2)-(b**2)),s*exp(-s)/((s**2)+(b**2))
    fs4=fs1-fs2+fs3
    print("Pregunta 1, b:")
    print(f"La antitransformada de Laplace para -1/(2(s+2)^2)+1/(2(s-2)^2) es:\n{inverse_laplace_transform(fs1,s,x)}\n")
    print(f"La antitransformada de Laplace para s*e^(-s)/((s^2)-(b^2)) es:\n{inverse_laplace_transform(fs2,s,x)}\n")
    print(f"La antitransformada de Laplace para s*e^(-s)/((s^2)+(b^2)) es:\n{inverse_laplace_transform(fs3,s,x)}\n")
    print(f"La antitransformada de Laplace para L1-L2+L3 (siendo estas L las funciones de Laplace dadas anteriormente) es:\n{inverse_laplace_transform(fs4,s,x)}\n")
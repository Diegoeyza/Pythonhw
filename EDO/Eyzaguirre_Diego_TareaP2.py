from sympy.integrals import laplace_transform, inverse_laplace_transform
from sympy.abc import x, s
from sympy import Symbol, exp, cos, sin, Heaviside
a =2
b =-3
fx =cos(x)
y0 = 1
fs = laplace_transform(fx, x, s, noconds=True)
Ys = a*y0/(a*s+b) + fs/(a*s+b)
yx = inverse_laplace_transform(Ys, s, x)
print(f"El resultado final de y(x) es: {yx}")

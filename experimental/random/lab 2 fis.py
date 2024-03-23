import math
mc=float(input("masa carro: "))
mp=float(input("masa peso: "))
a=int(input("ángulo: "))
r=a*3.1415926535/180
g=9.8
ac=g*(mp-mc*math.sin(r))/(mp+mc)
print(f"la aceleración es {ac}")
def fibonacci(n):
    l = [0,1]
    for i in range(n-2):
        l.append(l[-2:-1][0] + l[-1:][0])
    return l

lf = fibonacci(15)
suma = 0
for i in lf:
    suma += i

print(lf)
print(suma)
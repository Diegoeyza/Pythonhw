import random
n=int(input("ingrese un número de repeticiones"))
for i in range(1, n+1):
    a=str(random.randint(1,6))
    print(f"el numero es "+a)
compra=input()
lista=compra.split(",")
precios=[]
nombre=lista[0]
suma=[]
for i in range (1, len(lista)):
    lista[i]=int(lista[i])
for i in range(2, len(lista)):
    precios.append(lista[i])
precios.sort()
for i in range (0, lista[1]):
    suma.append(precios[i])
suma=sum(suma)
print(nombre+": $"+str(suma))


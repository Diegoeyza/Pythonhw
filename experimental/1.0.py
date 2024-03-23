datos=input()
datos=datos.split(" ")
orden=input()
orden=orden.split(" ")
for i in range (0, len(orden)):
	orden[i]=int(orden[i])
fin=datos[:]
for i in range(0, len(datos)):
    fin[orden[i]]=datos[i]
print(fin)

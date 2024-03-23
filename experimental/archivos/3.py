nombre=input()
lista=[]
listaB=[]
borrador=[]
a=""
with open("mejorescanciones.txt") as spotify:
    for i in spotify:
        lista.append(i.strip(","))
    for i in range (0, len(lista)):
        listaC=[]
        listaC.append(lista[i].strip(","))
        listaB.append(listaC)
    for i in lista:
        i=i.rstrip()
        borrador=i.split(",")
        if nombre in borrador[1]:
            print("Canción: "+borrador[0]+" - "+borrador[2])
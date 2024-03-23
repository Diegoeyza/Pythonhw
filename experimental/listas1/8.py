lista1=[]
lista2=[]
persona=" "
while persona!="end":
    persona=input()
    if persona!="end":
        persona=int(persona)
        if len(lista1)==0:
            lista1.append(persona)
        elif len(lista2)==0:
            lista2.append(persona)
        else:
            largo1=len(lista1)
            largo2=len(lista2)
            if largo1>largo2:
                largo=largo2
            elif largo2>=largo1:
                largo=largo1
            for i in range(0, largo):
                if lista1[i]<=lista2[i] and persona<lista1[i-1]:
                    lista1.insert(i, persona)
                elif lista2[i]<lista1[i] and persona<lista2[i-1]:
                    lista2.insert(i, persona)
                elif len(lista1)-1==i:
                    lista1.append(persona)
                elif len(lista2)-1==i:
                    lista2.append(persona)
print(f"{lista1}\n{lista2}")
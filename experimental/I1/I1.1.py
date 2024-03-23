hoyos=int(input())
tiros1=0
tiros2=0
for i in range (1,hoyos+1):
    distanciah=int(input())
    distancia1=distanciah
    distancia2=distanciah
    contador=1

    print("Hoyo "+str(i)+" - Distancia inicial: "+str(distanciah))
    while distancia1!=0 or distancia2!=0:
        if contador%2==1:
            if distancia1>0:
                golpe1=int(input())
                distancia1=distancia1-golpe1
                print("J1: "+str(golpe1))
                tiros1=tiros1+1
            elif distancia1<0:
                golpe1=int(input())
                distancia1=golpe1+distancia1
                print("J1: "+str(golpe1))
                tiros1=tiros1+1
        else:
            if distancia2>0:
                golpe2=int(input())
                distancia2=distancia2-golpe2
                print("J2: "+str(golpe2))
                tiros2=tiros2+1
            elif distancia2<0:
                golpe2=int(input())
                distancia2=golpe2+distancia2
                print("J2: "+str(golpe2))
                tiros2=tiros2+1
        contador=contador+1
    print("Puntaje actual J1: "+str(tiros1))
    print("Puntaje actual J2: "+str(tiros2))
if tiros1<tiros2:
    print("Gana J1")
elif tiros2<tiros1:
    print("Gana J2")
else:
    print("Empate!")
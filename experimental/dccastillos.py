print("¡Bienvenido/a a DCCastillos!")
print()
contador=1
castillo1=0
castilloA=0
castillo2=0
castilloB=0
color1="a"
color2="b"
colorA="c"
colorB="d"
diamante1=0
diamante2=0
hada1=0
hada2=0
while (castillo1)!=6 and (castillo2)!=6:
    cartas1=castillo1+castilloA+diamante1+hada1
    cartas2=castillo2+castilloB+diamante2+hada2
    costo_castillo1=1+(contador*(castillo1+castilloA+hada1))%4
    costo_castillo2=1+(contador*(castillo2+castilloB+hada2))%4
    if contador%2==1:
        print("Turno "+str(contador)+ " juega el jugador 1")
    elif contador%2==0:
        print("Turno "+str(contador)+ " juega el jugador 2")
    comando=str(input())
    if comando=="sacar carta":
        carta=str(input())
        print("Se saca la carta "+ (carta))
        if carta=="castillo":
            if contador%2==1:
                if color1=="a":
                    color1=str(input())
                    if color1!=color2:
                        print("Jugador 1 coleccionara castillos de color "+ color1)
                        castillo1=castillo1+1
                    elif color1==color2:
                        castilloA=castilloA+1
                        color1="a"
                else:
                    colorA=str(input())
                    if colorA==color1 and color2!=color1:
                        castillo1=castillo1+1
                    elif colorA==color2:
                        castilloA=castilloA+1
                    colorA="c"
            else:
                if color2=="b":
                    color2=str(input())
                    if color2!=color1:
                        print("Jugador 2 coleccionara castillos de color "+ color2)
                        castillo2=castillo2+1
                    elif color2==color1:
                        castilloB=castilloB+1
                        color2="b"
                else:
                    colorB=str(input())
                    if colorB==color2 and color2!=color1:
                        castillo2=castillo2+1
                    elif colorB==color1:
                        castilloB=castilloB+1
                    colorB="d"
            contador=contador+1
        elif carta=="diamante":
            if contador%2==1:
                diamante1=diamante1+1
            elif contador%2==0:
                diamante2=diamante2+1
            contador=contador+1
        elif carta=="hada":
            if contador%2==1:
                hada1=hada1+1
            elif contador%2==0:
                hada2=hada2+1
            contador=contador+1
        elif carta=="bruja":
            if contador%2==1:
                if cartas1==0:
                    print("No tienes cartas por perder")
                elif 2<=hada1-4/5*(castillo1):
                    hada1=hada1-1
                    print("¡Le has ganado a la bruja! Puedes conservar tus cartas a excepcion de una hada")
                else:
                    perdida1=1+((castillo1**2+hada1))%(diamante1+1)
                    for n in range (0, perdida1):
                        carta_perdida1=str(input())
                        if carta_perdida1=="hada" and hada1>0:
                            hada1=hada1-1
                        elif carta_perdida1=="diamante" and diamante1>0:
                            diamante1=diamante1-1
                        elif carta_perdida1=="castillo propio" and castillo1>0:
                            castillo1=castillo1-1
                        elif carta_perdida1=="castillo enemigo" and castilloA>0:
                            castilloA=castilloA-1
                    print("La bruja te ha quitado "+ str(perdida1)+ " cartas")
            else:
                if cartas2==0:
                    print("No tienes cartas por perder")
                elif 2<=hada2-4/5*(castillo2):
                    hada2=hada2-1
                    print("¡Le has ganado a la bruja! Puedes conservar tus cartas a excepcion de una hada")
                else:
                    perdida2=1+((castillo2**2+hada2))%(diamante2+1)
                    for n in range (0, perdida2):
                        carta_perdida2=str(input())
                        if carta_perdida2=="hada" and hada2>0:
                            hada2=hada2-1
                        elif carta_perdida2=="diamante" and diamante2>0:
                            diamante2=diamante2-1
                        elif carta_perdida2=="castillo propio" and castillo2>0:
                            castillo2=castillo2-1
                        elif carta_perdida2=="castillo enemigo" and castilloB>0:
                            castilloB=castilloB-1
                    print("La bruja te ha quitado "+ str(perdida2)+ " cartas")
            contador=contador+1
        print()
    elif comando=="comprar castillo":
        if contador%2==1:
            if color1!="a":
                if diamante1>=costo_castillo1:
                    if castilloB>=1:
                        print("El jugador 1 ha comprado una carta para su castillo "+str(color1))
                        castilloB=castilloB-1
                        castillo1=castillo1+1
                        diamante1=diamante1-costo_castillo1
                    else:
                        print("¡El jugador adversario no tiene cartas castillo de tu color!")
                else:
                    print("Necesitas al menos "+ str(costo_castillo1)+ " diamantes para comprar")
            
            else:
                print("¡Aun no tienes un color asignado, no puedes comprar!")  
        elif contador%2==0:
            if color2!="b":
                if diamante2>=costo_castillo2:
                    if castilloA>=1:
                        print("El jugador 2 ha comprado una carta para su castillo "+ str(color2))
                        castilloA=castilloA-1
                        castillo2=castillo2+1
                        diamante2=diamante2-costo_castillo2
                    else:
                        print("¡El jugador adversario no tiene cartas castillo de tu color!")
                else:
                    print("Necesitas al menos "+ str(costo_castillo2)+ " diamantes para comprar")
            else:
                print("¡Aun no tienes un color asignado, no puedes comprar!")  
        print()
        contador=contador+1
    else:
        print("Error 404, no se encuentra el comando: "+ (comando))
        print()
print(">>> ¡El juego DCCastillos ha terminado!")
if castillo1==6:
    print(">>> Ha ganado el jugador 1")
elif castillo2==6:
    print(">>> Ha ganado el jugador 2")
if color1=="a":
    print(">> El jugador 1 () tenia")
else:
    print(">> El jugador 1 "+"("+color1+")"+ " tenia")
print("Castillo(s) propio(s): "+str(castillo1))
print("Castillo(s) enemigo(s): "+str(castilloA))
print("Hada(s): "+str(hada1))
print("Diamante(s): "+str(diamante1))
if color2=="b":
    print(">> El jugador 2 () tenia")
else:
    print(">> El jugador 2 "+"("+color2+")"+ " tenia")
print("Castillo(s) propio(s): "+str(castillo2))
print("Castillo(s) enemigo(s): "+str(castilloB))
print("Hada(s): "+str(hada2))
print("Diamante(s): "+str(diamante2))
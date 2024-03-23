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
            contador=contador+1
        print()
    elif comando=="comprar castillo":
        print("¡Aun no puedes comprar castillos!")
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
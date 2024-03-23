class CeldaSuperior:
    
    def __init__(self):
        self.n_jugadores=0
        self.objetivo=" "
    
    def __str__(self):
        a=f"Esta celda contiene al objetivo {self.objetivo} y esta ocupada por {self.n_jugadores} jugador(es)"
        b=f"Esta celda contiene al objetivo {self.objetivo}"
        if self.n_jugadores>0:
            return a
        else:
            return b
class CeldaInferior:
    def __init__(self):
        self.arriba=False
        self.abajo=False
        self.izquierda=False
        self.derecha=False
    
    def poner_paredes(self, paredes):
        for i in range (len(paredes)):
            if paredes[i]=="arriba":
                self.arriba=True
            
            elif paredes[i]=="abajo":
                self.abajo=True
            
            elif paredes[i]=="izquierda":
                self.izquierda=True
            
            elif paredes[i]=="derecha":
                self.derecha=True

    def __str__(self):
        a=f"Pared arriba: {self.arriba}\nPared abajo: {self.abajo}\nPared derecha: {self.derecha}\nPared izquierda: {self.izquierda}"
        return a


class Mago:
    def __init__(self, nombre):
        self.nombre=nombre
        self.objetivos_completados=[]
        self.objetivo=" "
        self.fila=0
        self.columna=0
        self.caidas=0
        self.espacios_avanzados=0
        if self.objetivo==" ":
            self.sacar_nuevo_objetivo()
    
    def __str__(self):
        a=f"Jugador {self.nombre} | puntaje: {len(self.objetivos_completados)} objetivo: {self.objetivo} | caidas: {self.caidas} pasos: {self.espacios_avanzados}"
        return a
    
    def sacar_nuevo_objetivo(self):
        juan=input()
        if self.objetivo!=" ":
            x=self.objetivo
            self.objetivos_completados.append(x)
            print(f"{self.nombre} ha llegado a su objetivo: {self.objetivo}\nHa recolectado {len(self.objetivos_completados)} en total")
        self.objetivo=juan
        print(f"Nuevo objetivo de {self.nombre}: {self.objetivo}")
        return self.objetivo
    
    def jugar_turno(self):
        import random
        mov=[]
        for i in range (0, random.randint(1, 6)):
            x=input()
            mov.append(x)
            
        return mov
class Tablero:
    def __init__(self, ancho, alto):
        self.ancho=ancho
        self.alto=alto
        tablainf=[]
        tablasup=[]
        for j in range(0, alto):
            tablainf.append([])
            tablasup.append([])
            for i in range (0, ancho):
                celda_superior = CeldaSuperior()
                celda_inferior=CeldaInferior()
                tablasup[j].append(celda_superior)
                tablainf[j].append(celda_inferior)
        self.nivel_inferior=tablainf
        self.nivel_superior=tablasup
    def cargar_tablero(self):
        with open ("tablero_superior.txt") as x:
            for i in x:
                
                a=i.split(" ")
                fila=int(a[0])
                col=int(a[1])
                a[2]=a[2].strip("\n")
                
                self.nivel_superior[fila][col].objetivo=a[2]

        with open ("tablero_inferior.txt") as x:
            for i in x:
                a=i.split(",")
                a[2]=a[2].strip("\n")
                a[2]=a[2].split(";")
                
                fila=int(a[0])
                col=int(a[1])
                self.nivel_inferior[fila][col].poner_paredes(a[2])
    def mover_jugador(self, jugador, movimiento):
        jugador.sacar_nuevo_objetivo
        fila=jugador.fila
        columna=jugador.columna
        if movimiento=="arriba":
            if fila-1<0:
                return "fuera"
            else:
                if self.nivel_superior[fila-1][columna].n_jugadores>0:
                    return "espacio ocupado"
                elif self.nivel_inferior[fila][columna].arriba==True:
                    return "pared"
                else:
                    self.nivel_superior[fila][columna].n_jugadores=0
                    jugador.fila=jugador.fila-1
                    return "movimiento exitoso"
                    
        elif movimiento=="abajo":
            if fila+1>self.alto-1:
                return "fuera"
            else:
                if self.nivel_superior[fila+1][columna].n_jugadores>0:
                    return "espacio ocupado"
                elif self.nivel_inferior[fila][columna].abajo==True:
                    return "pared"
                else:
                    self.nivel_superior[fila][columna].n_jugadores=0
                    jugador.fila=jugador.fila+1
                    return "movimiento exitoso"
        
        elif movimiento=="izquierda":
            if columna-1>=0:
                if self.nivel_superior[fila][columna-1].n_jugadores>0:
                    return "espacio ocupado"
                elif self.nivel_inferior[fila][columna].izquierda==True:
                    return "pared"
                else:
                    self.nivel_superior[fila][columna].n_jugadores=0
                    print(jugador.columna)
                    jugador.columna=jugador.columna-1
                    print(jugador.columna)
                    return "movimiento exitoso"
            elif columna-1<0:
                return "fuera"
        
        elif movimiento=="derecha":
            if columna+1>self.ancho-1:
                return "fuera"
            else:
                if self.nivel_superior[fila][columna+1].n_jugadores>0:
                    return "espacio ocupado"
                elif self.nivel_inferior[fila][columna].derecha==True:
                    return "pared"
                else:
                    self.nivel_superior[fila][columna].n_jugadores=0
                    jugador.columna=jugador.columna+1
                    return "movimiento exitoso"











# ====================== #
# NO EDITES LO SIGUIENTE #
# ====================== #
import funciones


ancho = int(input())
alto = int(input())
tablero = Tablero(ancho, alto)
tablero.cargar_tablero()
nombre_mago = input()
# va a pedir input dentro de la instanciación.
jugador = Mago(nombre_mago)  # parte en (0,0)
# el mago está en (0, 0)
tablero.nivel_superior[0][0].n_jugadores = 1

jugadas = jugador.jugar_turno()
for jugada in jugadas:
    print(tablero.mover_jugador(jugador, jugada))
    funciones.imprimir_tablero_mago(tablero, jugador)

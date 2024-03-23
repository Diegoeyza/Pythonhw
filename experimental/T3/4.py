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
                a[2].strip("\n")
                self.nivel_superior[fila][col].objetivo=a[2]

        with open ("tablero_inferior.txt") as x:
            for i in x:
                a=i.split(",")
                a[2].split(";")
                fila=int(a[0])
                col=int(a[1])
                self.nivel_inferior[fila][col].objetivo=a[2]
                


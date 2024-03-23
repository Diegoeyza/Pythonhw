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
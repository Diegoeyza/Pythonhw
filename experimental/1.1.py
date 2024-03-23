class Jugador:
    def __init__(self, nombre, vida, exp):
        self.nombre=nombre
        self.vida=vida
        self.exp=exp
        self.monedas=0
    def tomar_pocion_exp(self, tamano):
        if self.monedas>4:
            if tamano=="grande":
                self.exp=self.exp+5
                self.monedas=self.monedas-5
                return True
            elif tamano=="chica":
                self.monedas=self.monedas-5
                self.exp=self.exp+3
                return True
            return False
        return False
    def tomar_pocion_vida(self, tamano):
        if self.exp>=5:
            if tamano=="grande":
                self.exp=self.exp-5
                self.vida=self.vida+5
                return True
            elif tamano=="chica":
                self.vida=self.vida+3
                self.exp=self.exp-5
                return True
            return False
        return False
                
    def luchar(self, oponente):
        fuerza=self.vida+self.exp
        if fuerza>=oponente:
            return True
        else:
            self.vida=0
            return False
            
    def __str__(self):
        a=f"------ RESUMEN RONDA ------\nNombre: {self.nombre}\nVida: {self.vida}\nExperiencia: {self.exp}\nMonedas: {self.monedas}"
        return a
        
        
        
def comenzar_aventura(jugador, eventos):
    contador=0
    while contador<len(eventos):
        if eventos[contador]=="pocion exp chica":
            result=jugador.tomar_pocion_exp("chica")
            if result==False:
                print(">> No me alcanzan las monedas para tomar la pocion")
            else:
                print(">> He tomado la pocion de experiencia")
        elif eventos[contador]=="pocion exp grande":
            result=jugador.tomar_pocion_exp("grande")
            if result==False:
                print(">> No me alcanzan las monedas para tomar la pocion")
            else:
                print(">> He tomado la pocion de experiencia")
        elif eventos[contador]=="pocion vida chica":
            result=jugador.tomar_pocion_vida("chica")
            if result==False:
                print(">> No me alcanza la experiencia para tomar la pocion")
            else:
                print(">> He tomado la pocion de vida")
        elif eventos[contador]=="pocion vida grande":
            result=jugador.tomar_pocion_vida("grande")
            if result==False:
                print(">> No me alcanza la experiencia para tomar la pocion")
            else:
                print(">> He tomado la pocion de vida")
        elif eventos[contador]=="bolsa de monedas":
            jugador.monedas=jugador.monedas+4
            print(">> Encontre monedas")
        else:
            result=jugador.luchar(int(eventos[contador]))
            if result==True:
                print(f">> Gane el combate")
            else:
                print(f">> Fui derrotado")
                contador=len(eventos)
        print(jugador)
        print("")
        contador+=1
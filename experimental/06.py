class Superheroe:
    def __init__(self, nombre, vida, fuerza, defensa):
        self.nombre=nombre
        self.vida=vida
        self.fuerza=fuerza
        self.defensa=defensa
        return None
    def golpear(superheroe, otro_superheroe):
      daño=max(superheroe.fuerza - otro_superheroe.defensa, 0)
      return daño
      
rounds=0
def combate(superheroe_1, superheroe_2, rounds):
    contador=1
    while superheroe_1.vida>0 and superheroe_2.vida>0 and rounds>contador:
        if contador%2==1:
            superheroe_2.vida=superheroe_2.vida-(superheroe_1.golpear(superheroe_2))
        elif contador%2==0:
            superheroe_1.vida=superheroe_1.vida-(superheroe_2.golpear(superheroe_1))
        contador+=1
    if superheroe_1.vida>0 and superheroe_1.vida>superheroe_2.vida:
        print(f"Ganador: {superheroe_1.nombre} {superheroe_1.vida}, {superheroe_2.nombre} {superheroe_2.vida}")
    else:
        print(f"Ganador: {superheroe_2.nombre} {superheroe_2.vida}, {superheroe_1.nombre} {superheroe_1.vida}")
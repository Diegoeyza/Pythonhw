# Crea tu clase aqui
class CeldaSuperior:
    def __init__(self):
        self.n_jugadores=0
        self.objetivo=""
    
    def __str__(self):
        a=f"Esta celda contiene al objetivo {self.objetivo} y esta ocupada por {self.n_jugadores} jugador(es)"
        b=f"Esta celda contiene al objetivo {self.objetivo}"
        if self.n_jugadores>0:
            return a
        else:
            return b







### NO MODIFICAR ###
# Flujo de ejecucion
num_de_celdas = int(input())

for num in range(num_de_celdas):
    jugador_objetivo = input().split(',')
    jugador = int(jugador_objetivo[0])
    objetivo = jugador_objetivo[1]
    celda_superior = CeldaSuperior()

    celda_superior.n_jugadores = jugador
    celda_superior.objetivo = objetivo
    print(celda_superior)
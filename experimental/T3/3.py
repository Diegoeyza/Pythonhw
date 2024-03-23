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
        self.sacar_nuevo_objetivo=input()
        if self.objetivo!=" ":
            x=self.objetivo
            self.objetivos_completados.append(x)
            print(f"{self.nombre} ha llegado a su objetivo: {self.objetivo}\nHa recolectado {len(self.objetivos_completados)} en total")
        self.objetivo=self.sacar_nuevo_objetivo
        print(f"Nuevo objetivo de {self.nombre}: {self.objetivo}")
        return self.objetivo
    
    def jugar_turno(self):
        import random
        mov=[]
        for i in range (0, random.randint(1, 6)):
            x=input()
            mov.append(x)
            
        return mov

mago_1 = Mago(input())
mago_2 = Mago(input())
# Se mueve cada jugador
movimientos = mago_1.jugar_turno()
print("\nEs el turno de", mago_1.nombre)
for direccion in movimientos:
    print(mago_1.nombre, 'se mueve a la direccion:', direccion)
    # Se va a simular la captura de un objetivo
    # en el caso que el mago se mueva a la derecha
    if direccion == 'derecha':
        mago_1.sacar_nuevo_objetivo()

print("\nEs el turno de", mago_2.nombre)
movimientos = mago_2.jugar_turno()
for direccion in movimientos:
    print(mago_2.nombre, 'se mueve a la direccion:', direccion)
    if direccion == 'derecha':
        mago_2.sacar_nuevo_objetivo()
        print("a")

# Finalmente vemos el estado de los jugadores
print()
print(mago_1)
print(mago_2)
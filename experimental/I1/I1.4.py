class Auto: # class para indicar que es una clase y el nombre de la clase partiendo con mayúscula
    def __init__(self, marca, motor, color, puertas, ruedas): # parámetros necesarios para que exista la clase
        self.marca = marca  # self.marca es un atributo de la instancia a crear de la clase Auto
        self.motor = motor
        self.color = color
        self.num_puertas = puertas
        self.num_ruedas = ruedas
auto_creado_1 = Auto("Jeep", "24V", "rojo", 5, 4)
auto_creado_2 = Auto("Toyota", "16V", "blanco", 2, 4)
print (auto_creado_1.color)
import csv
class Mamaguevo:
    def __init__(self, mamaguevadas, huevos):
        self.mamamguevadas=mamaguevadas
        self.huevos=huevos
    def cagaso(self, x):
        if self.huevos==0:
            print("valiste kbron")
        elif self.huevos>0:
            self.mamaguevadas+=x
            print(f"Te quedan {self.huevos} oportunidades")
    def ayuda(self):
        self.huevos+=1

Marco=Mamaguevo(0,2)
print(f"{Marco.mamamguevadas}")

class Life:
    def __init__(self, age):
        self.age=age
        self.alive=1
    def death(self):
        self.alive=0
    def check_health(self):
        if self.alive==1:
            print("alive")
        else:
            print("dead")
class Mammal(Life):
from PIL import Image
from PIL import ImageDraw
from abc import ABC, abstractmethod


class Project:
    def __init__(self, filename):
        self.Img = Image.open(filename).convert('RGB')
        self.Img.save(f'Modificado_{filename}')
        self.Img = Image.open(f'Modificado_{filename}').convert('RGB')
        self.filename = filename
    
    def show_image(self):
        self.Img.show()

#class Filters(ABC):         #defino la clase abstracta madre de la que van a heredar todos los filtros
#    @abstractmethod
#    def Save(self):
#        pass

class Draw_line(Project):
    def __init__(self, filename):
        super().__init__(filename)
    
    def Drawing(self):
        Draw = ImageDraw.Draw(self.Img)
        Draw.line((0,0) + self.Img.size, fill=(200, 000, 200), width=10)
        self.Img.show()
        self.Img.save(f'Modificado_{self.filename}')

class Directory:
    def __init__(self):
        self.Dict={"Project":[],"File":[],"Changes":[],"Checkpoint":[]}

exit=0
while (exit==0):
    print(f"Welcome to Pillow Image editor, please select one of the following commands:\n-To start a project type 0\n-To show an image type 1\n-To close the editor type END")
    Dibujado = Draw_line('SavedSparkleOn.png')
    Dibujado.Drawing()
    break


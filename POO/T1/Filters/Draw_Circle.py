from Filters.Filter import Filter
from PIL import ImageDraw

class Draw_circle(Filter):
    def __init__(self, position, db):
        super().__init__(position, db)
    def Apply(self, x, y, size, color):
        Draw = ImageDraw.Draw(self.Img)
        Draw.ellipse([(x, y), (x+size, y+size)], None, color)
        self.Img.show()
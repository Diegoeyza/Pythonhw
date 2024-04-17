from Filters.Filter import Filter
from PIL import ImageDraw

class Draw_line(Filter):
    def __init__(self, position, db):
        super().__init__(position, db)
    
    def Apply(self, color):
        Draw = ImageDraw.Draw(self.Img)
        Draw.line((0,0) + self.Img.size, fill=(color), width=10)
        self.Img.show()
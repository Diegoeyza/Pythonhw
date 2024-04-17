from Filters.Filter import Filter
from PIL import ImageDraw

class Write_text(Filter):
    def __init__(self, position, db):
        super().__init__(position, db)
    def Apply(self, x, y, text, size, color):
        Draw = ImageDraw.Draw(self.Img)
        Draw.text((x, y), text, color, font_size=size)
        self.Img.show()
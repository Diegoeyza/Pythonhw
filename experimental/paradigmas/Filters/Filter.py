from abc import ABC
from PIL import Image

class Filter:
    def __init__(self, position, db):
        self.Img = Image.open(db[position]).convert('RGB')
    
    def show_image(self):
        self.Img.show()
from PIL import Image

class Filter:
    def __init__(self, position, db):
        self.Img = Image.open(db[position]).convert('RGB')
    
    def show_image(self):
        self.Img.show()
    def show_size(self):
        print(f"Current image size is {self.Img.width}x{self.Img.height}")
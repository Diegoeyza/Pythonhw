from PIL import Image
from Filters.Filter import Filter

class Fuse(Filter):
    def __init__(self, position, filename2, db):
        super().__init__(position, db)
        self.Img2 = Image.open(filename2).convert('RGB')
        self.Pxls1 = (self.Img).load()
        self.Img2 = (self.Img2).resize((((self.Img).size)[0], ((self.Img).size)[1]))
        self.Pxls2 = (self.Img2).load()
        
    def Apply(self):
        for j in range(((self.Img).size)[1]):
            for i in range(((self.Img).size)[0]):
                (self.Pxls1)[i, j] = (int(((((self.Pxls1)[i, j])[0]) + (((self.Pxls2)[i, j])[0]))/2), int(((((self.Pxls1)[i, j])[1]) + (((self.Pxls2)[i, j])[1]))/2), int(((((self.Pxls1)[i, j])[2]) + (((self.Pxls2)[i, j])[2]))/2))
        self.show_image()
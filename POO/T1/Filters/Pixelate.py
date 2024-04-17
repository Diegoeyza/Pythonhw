from Filters.Filter import Filter
from PIL import Image

class Pixelate(Filter):
    def __init__(self, position, PxlSize,db):
        super().__init__(position,db)
        self.PxlSize = PxlSize

    def Apply(self):

        Shrinked = (self.Img).resize((self.PxlSize, self.PxlSize), resample=Image.Resampling.BILINEAR)
        (self.Img) = Shrinked.resize((self.Img).size, Image.Resampling.NEAREST)
        self.Img.show()
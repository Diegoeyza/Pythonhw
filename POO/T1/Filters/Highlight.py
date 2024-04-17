from Filters.Filter import Filter

class Highlight(Filter):
    def __init__(self, position, valuer, valueg, valueb, tolerance, db):
        super().__init__(position, db)
        self.Pxls = self.Img.load()
        self.valuer = valuer
        self.valueg = valueg
        self.valueb = valueb
        self.tolerance = tolerance
    def Apply(self):
        for j in range(self.Img.size[1]):
            for i in range(self.Img.size[0]):
                if(((self.valuer-self.tolerance) < self.Pxls[i, j][0] < (self.valuer+self.tolerance)) and ((self.valueg-self.tolerance) < self.Pxls[i, j][1] < (self.valueg+self.tolerance)) and ((self.valueb-self.tolerance) < self.Pxls[i, j][2] < (self.valueb+self.tolerance))):
                    ...
                else:
                    self.Pxls[i, j] = (int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3), int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3), int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3))
        self.show_image()
from Filters.Filter import Filter


class Resize(Filter):
    def __init__(self, position, db):
        super().__init__(position,db)
        
    def Apply(self, width, height):
        self.Img = self.Img.resize((width, height))
        self.Img.show()
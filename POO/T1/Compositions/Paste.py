from Filters.Filter import Filter
from PIL import Image

class Paste_Right(Filter):
    def __init__(self, position, db):
        super().__init__(position, db)
    def Paste(self,filename2):
        self.Img2 = Image.open(filename2).convert('RGB')  
        self._size1 = [(self.Img).width,(self.Img).height]
        print((self.Img).width)
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (self._size2[0]+self._size1[0],max(self._size2[1],self._size1[1])))

        (self.background).paste(self.Img,(0,0))
        (self.background).paste(self.Img2,(self._size1[0]+1,0))
        (self.background).show()
        self.Img = self.background

class Paste_Left(Filter):
    def __init__(self, position, db):
        super().__init__(position, db)
    def Paste(self,filename2):
        self.Img2 = Image.open(filename2).convert('RGB')  
        self._size1 = [(self.Img).width,(self.Img).height]
        print((self.Img).width)
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (self._size2[0]+self._size1[0],max(self._size2[1],self._size1[1])))

        (self.background).paste(self.Img2,(0,0))
        (self.background).paste(self.Img,(self._size2[0]+1,0))
        (self.background).show()
        self.Img = self.background

class Paste_Below(Filter):
    def __init__(self, position, db):
        super().__init__(position, db)
    def Paste(self,filename2):
        self.Img2 = Image.open(filename2).convert('RGB')
        self._size1 = [(self.Img).width,(self.Img).height]
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (max(self._size2[0],self._size1[0]), self._size2[1]+self._size1[1]))

        (self.background).paste(self.Img,(0,0))
        (self.background).paste(self.Img2,(0,self._size1[1]+1))
        (self.background).show()
        self.Img = self.background

class Paste_Over(Filter):
    def __init__(self, position, db):
        super().__init__(position, db)
    def Paste(self,filename2):
        self.Img2 = Image.open(filename2).convert('RGB')  
        self._size1 = [(self.Img).width,(self.Img).height]
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (max(self._size2[0],self._size1[0]), self._size2[1]+self._size1[1]))

        (self.background).paste(self.Img2,(0,0))
        (self.background).paste(self.Img,(0,self._size2[1]+1))
        (self.background).show()
        self.Img = self.background
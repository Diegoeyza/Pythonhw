from PIL import Image
from PIL import ImageDraw
from Filters import Filter

def FileCheck(file):
    Check = 0
    while Check != 1:
        try:
            Opened = Image.open(file).convert('RGB')
            Opened.close()
        except IOError:
             print("No such file or directory, try again")
             file = input("Insert image path:\n")
        else:
            Check = 1
            return file

class Directory:
    def __init__(self):
        self.Dict={"Project":[],"File":[],"Changes":[],"Checkpoint":[]}
        self.position=0


    def New_project(self,name,file):
        (self.Dict["Project"]).append(name)
        (self.Dict["File"]).append(file)
        (self.Dict["Checkpoint"]).append(file)
        (self.Dict["Changes"]).append("Changes:")
    

    def Change(self, change, file,position):
        (self.Dict["Checkpoint"])[position]=(self.Dict["File"])[position]
        (self.Dict["File"])[position]=file
        (self.Dict["Changes"])[position]+=f" {change}/ "  #escribe el cambio hecho en cuestión

    def Undo(self,position):
        if (self.Dict["File"][position]!=self.Dict["Checkpoint"][position]):
            self.Dict["File"][position]=self.Dict["Checkpoint"][position]
    
    def _print(self):
        print(self.Dict)

#Dir.Dict["File"]

class Draw_line(Filter):
    def __init__(self, position, db):
        super().__init__(position, db)
    
    def Apply(self):
        Draw = ImageDraw.Draw(self.Img)
        Draw.line((0,0) + self.Img.size, fill=(200, 000, 200), width=10)
        self.Img.show()

class Draw_circle(Filter):
    def __init__(self, position,db):
        super().__init__(position,db)
    def Apply(self, x, y, size, color):
        Draw = ImageDraw.Draw(self.Img)
        Draw.ellipse([(x, y), (x+size, y+size)], None, color)
        self.Img.show()

class Write_text(Filter):
    def __init__(self, position,db):
        super().__init__(position,db)
    def Apply(self, x, y, text, size, color):
        Draw = ImageDraw.Draw(self.Img)
        Draw.text((x, y), text, color, font_size=size)
        self.Img.show()

class Pixeleado(Filter):
    def __init__(self, position, PxlSize,db):
        super().__init__(position,db)
        self.PxlSize = PxlSize

    def Apply(self):

        Shrinked = (self.Img).resize((self.PxlSize, self.PxlSize), resample=Image.Resampling.BILINEAR)
        (self.Img) = Shrinked.resize((self.Img).size, Image.Resampling.NEAREST)
        self.Img.show()

class Fuse(Filter):
    def __init__(self, position, filename2,db):
        super().__init__(position,db)
        self.Img2 = Image.open(filename2).convert('RGB')
        self.Pxls1 = (self.Img).load()
        self.Img2 = (self.Img2).resize((((self.Img).size)[0], ((self.Img).size)[1]))
        self.Pxls2 = (self.Img2).load()
        
    def Apply(self):
        for j in range(((self.Img).size)[1]):
            for i in range(((self.Img).size)[0]):
                (self.Pxls1)[i, j] = (int(((((self.Pxls1)[i, j])[0]) + (((self.Pxls2)[i, j])[0]))/2), int(((((self.Pxls1)[i, j])[1]) + (((self.Pxls2)[i, j])[1]))/2), int(((((self.Pxls1)[i, j])[2]) + (((self.Pxls2)[i, j])[2]))/2))
        self.show_image()

class Resize(Filter):
    def __init__(self, position, width, height,db):
        super().__init__(position,db)
        self.Img = self.Img.resize((width, height))
        self.Img.show()

class GrayScale(Filter):
    def __init__(self, position,db):
        super().__init__(position,db)
        self.Pxls = (self.Img).load()

    def Apply(self):
        for j in range(self.Img.size[1]):
            for i in range(self.Img.size[0]):
                self.Pxls[i, j] = (int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3), int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3), int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3))
        self.show_image()

class Paste_X(Filter):
    def __init__(self, position,db):
        super().__init__(position,db)
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

class Paste_Y(Filter):
    def __init__(self, position,db):
        super().__init__(position,db)
    def Paste(self,filename2):
        self.Img2 = Image.open(filename2).convert('RGB')  
        self._size1 = [(self.Img).width,(self.Img).height]
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (max(self._size2[0],self._size1[0]), self._size2[1]+self._size1[1]))

        (self.background).paste(self.Img,(0,0))
        (self.background).paste(self.Img2,(0,self._size1[1]+1))
        (self.background).show()
        self.Img = self.background
class Negative(Filter):
    def __init__(self, position,db):
        super().__init__(position,db)
        self.Pxls = self.Img.load()

    def Apply(self):
        for j in range(self.Img.size[1]):
            for i in range(self.Img.size[0]):
                self.Pxls[i, j] = ((255 - self.Pxls[i, j][0]), (255 - self.Pxls[i, j][1]), (255- self.Pxls[i, j][2]))
        self.show_image()

class Highlight(Filter):
    def __init__(self, position, valuer, valueg, valueb, tolerance,db):
        super().__init__(position,db)
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

class Menu():
    def __init__(self):
        self.exit="0"
        self.entry=""

    def Start(self):
        while(self.exit=="0"):
            self.entry=input(f"\nWelcome to Pillow Image editor, please select one of the following commands:\n-To start a project, type 0\n-To work on an existing project, type 1\n-To show an image from a project, type 2\n-To close the editor, type END\n")
            if (self.entry=="END" or self.entry=="End" or self.entry=="end"):
                self.exit=1
            
            elif (self.entry=="0"):
                self.pexit=0
                self.position=0
                pname=input("Please enter the name you will give to your new project (it must be unique): ")
                self.pfile=FileCheck(input("Please enter the path of the picture you want to edit: "))

                Im = Image.open(self.pfile).convert('RGB') ##Para que no sobreescriva todo el rato las imagenes de base
                Im.save(f'Edited_{self.pfile}')

                Dir.New_project(pname, f'Edited_{self.pfile}')
                self.position=Dir.Dict["Project"].index(pname)
            
            elif (self.entry=="1"):
                if (len(Dir.Dict["Project"])==0):
                    print("There are no projects available, please create a new one at the menu\n")
                    continue
                
                elif (len(Dir.Dict["Project"])!=0):
                    self.position=0
                    self.pexit=0
                    print("\nThe projects that are available are: ")
                    for i in range (0, len(Dir.Dict["Project"])):
                        print(f"-{i}: ",end="")
                        print(Dir.Dict["Project"][i])
                    self.position=int(input("Please select a project to open by entering its index number: "))
            
            elif (self.entry=="2"):
                if (len(Dir.Dict["Project"])==0):
                    print("There are no projects yet\n")
                    continue
                elif (len(Dir.Dict["Project"])!=0):
                        self.position=0
                        self.pexit=0
                        print("\nThe projects that are available are: ")
                        for i in range (0, len(Dir.Dict["Project"])):
                            print(f"-{i}: ",end="")
                            print(Dir.Dict["Filter"][i])
                        self.position=int(input("Please select a project to show by entering its index number: "))
                        print("Loading image...")
                        Display=Filter(self.position,Dir.Dict["File"])
                        Display.show_image()
            
            if ((self.entry=="0"or self.entry=="1")and 0<=self.position<len(Dir.Dict["Project"])):
                while (self.pexit==0):
                    efile=Dir.Dict["File"][self.position]
                    self.edit=input(f"\nPlease select what do you want to do to {efile}:\n-To draw select 0\n-To pixelate select 1\n-To fuse it with another image select 2\n-To apply grayscale to the image select 3\n-To paste another image select 4\n-To apply a negative filter select 5\n-To apply highlight select 6\n-To rezise image select 7\n-To leave this project type END\n")
                    if (self.edit=="end" or self.edit=="END" or self.edit=="End"):
                        self.pexit=1
                    elif (self.edit=="0"):
                        ColorChoice = input("Select a color:\n-1 Blue\n-2 Red\n-3 Black\n-4 White\n-5 Green\n-6 Pink\n")
                        if (ColorChoice == "1"):
                            Color = (0,0,255)
                        elif (ColorChoice == "2"):
                            Color = (255,0,0)
                        elif (ColorChoice == "3"):
                            Color = (0,0,0)
                        elif (ColorChoice == "4"):
                            Color = (255,255,255)
                        elif (ColorChoice == "5"):
                            Color = (0,255,0)
                        else:
                            Color = (200,0,200)
                        choice = input("-To draw a line select 1\n-To draw a circle select 2\n-To write text select 3\n")
                        if (choice == "1"):
                            ImgDrawn = Draw_line(self.position)
                            ImgDrawn.Apply()
                            ImgDrawn.Img.save(Dir.Dict["File"][self.position])
                            Dir.Change("Drawn_line", Dir.Dict["File"][self.position], self.position)

                        elif (choice == "2"):
                            ImgCircle = Draw_circle(self.position)
                            print("Select x and y coordinate (From upper left corner)")
                            Imgx = int(input("x: "))
                            Imgy = int(input("y: "))
                            Size = int(input("Select size in pixels\n"))
                            
                            ImgCircle.Apply(Imgx, Imgy, Size, Color)
                            ImgCircle.Img.save(Dir.Dict["File"][self.position])
                            Dir.Change("Circle", Dir.Dict["File"][self.position], self.position)
                        elif (choice == "3"):
                            ImgWrite = Write_text(self.position)
                            print("Select x and y coordinate (From upper left corner)")
                            Imgx = int(input("x: "))
                            Imgy = int(input("y: "))
                            Size = int(input("Select size\n"))
                            text = input("Type in text to be used\n")
                            ImgWrite.Apply(Imgx, Imgy, text, Size, Color)
                            ImgWrite.Img.save(Dir.Dict["File"][self.position])
                            Dir.Change("Text", Dir.Dict["File"][self.position], self.position)

                    elif (self.edit=="1"):
                        Pxl =int(input("Insert pixel amount\n"))
                        ImgPixelated = Pixeleado(self.position, Pxl, Dir.Dict["File"])
                        ImgPixelated.Apply()
                        ImgPixelated.Img.save(Dir.Dict["File"][self.position])
                        Dir.Change("Pixelated", Dir.Dict["File"][self.position], self.position)

                    elif (self.edit=="2"):
                        file2 = FileCheck(input("Insert path for the second image:\n"))
                        ImgFused = Fuse(self.position, file2)
                        ImgFused.Apply()
                        ImgFused.Img.save(Dir.Dict["File"][self.position])
                        Dir.Change("Fused", Dir.Dict["File"][self.position], self.position)
                    
                    elif (self.edit=="3"):
                        ImgGrayScaled = GrayScale(self.position)
                        ImgGrayScaled.Apply()
                        ImgGrayScaled.Img.save(Dir.Dict["File"][self.position])
                        Dir.Change("Gray_scaled", Dir.Dict["File"][self.position], self.position)
                    
                    elif(self.edit=="4"):
                        file2 = FileCheck(input("Insert path for the second image:\n"))
                        choice = input("Type 1 to paste on under, type 2 to paste on the side\n")
                        if(choice == "1"):
                            ImgPastedY = Paste_Y(self.position)
                            ImgPastedY.Paste(file2)
                            ImgPastedY.Img.save(Dir.Dict["File"][self.position])
                            Dir.Change("PastedY", Dir.Dict["File"][self.position], self.position)
                        elif(choice == "2"):
                            ImgPastedX = Paste_X(self.position)
                            ImgPastedX.Paste(file2)
                            ImgPastedX.Img.save(Dir.Dict["File"][self.position])
                            Dir.Change("PastedX", Dir.Dict["File"][self.position], self.position)
                        else:
                            print("Invalid")

                    elif(self.edit=="5"):
                        ImgNegative = Negative(self.position)
                        ImgNegative.Apply()
                        ImgNegative.Img.save(Dir.Dict["File"][self.position])
                        Dir.Change("Negative", Dir.Dict["File"][self.position], self.position)
                    
                    elif(self.edit=="6"):
                        ValueR = int(input("Insert R: "))
                        ValueG = int(input("Insert G: "))
                        ValueB = int(input("Insert B: "))
                        Tolerance = int(input("Insert a tolerance: "))

                        ImgHighlight = Highlight(self.position, ValueR, ValueG, ValueB, Tolerance)
                        ImgHighlight.Apply()
                        ImgHighlight.Img.save(Dir.Dict["File"][self.position])
                        Dir.Change("Highlight", Dir.Dict["File"][self.position], self.position)
                    elif(self.edit=="7"):
                        Width = int(input("Width: "))
                        Height = int(input("Height: "))
                        ImgResize = Resize(self.position, Width, Height)
                        ImgResize.Img.save(Dir.Dict["File"][self.position])
                        Dir.Change("Resize", Dir.Dict["File"][self.position], self.position)

                
Dir=Directory()
menu=Menu()
menu.Start()




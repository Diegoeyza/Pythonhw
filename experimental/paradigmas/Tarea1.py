from PIL import Image
from PIL import ImageDraw


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



class Project:
    def __init__(self, position):
        self.Img = Image.open(Dir.Dict["File"][position]).convert('RGB')
    
    def show_image(self):
        self.Img.show()

class Draw_line(Project):
    def __init__(self, position):
        super().__init__(position)
    
    def Apply(self):
        Draw = ImageDraw.Draw(self.Img)
        Draw.line((0,0) + self.Img.size, fill=(200, 000, 200), width=10)
        self.Img.show()

class Pixeleado(Project):
    def __init__(self, position, PxlSize):
        super().__init__(position)
        self.PxlSize = PxlSize

    def Apply(self):

        Shrinked = (self.Img).resize((self.PxlSize, self.PxlSize), resample=Image.Resampling.BILINEAR)
        self.Img.show()
        (self.Img) = Shrinked.resize((self.Img).size, Image.Resampling.NEAREST)
        self.Img.show()

class Fuse(Project):
    def __init__(self, position, filename2):
        super().__init__(position)
        self.Img2 = Image.open(filename2).convert('RGB')
        self.Pxls1 = (self.Img).load()
        self.Img2 = (self.Img2).resize((((self.Img).size)[0], ((self.Img).size)[1]))
        self.Pxls2 = (self.Img2).load()
        
    def Apply(self):
        for j in range(((self.Img).size)[1]):
            for i in range(((self.Img).size)[0]):
                (self.Pxls1)[i, j] = (int(((((self.Pxls1)[i, j])[0]) + (((self.Pxls2)[i, j])[0]))/2), int(((((self.Pxls1)[i, j])[1]) + (((self.Pxls2)[i, j])[1]))/2), int(((((self.Pxls1)[i, j])[2]) + (((self.Pxls2)[i, j])[2]))/2))
        self.show_image()

class GrayScale(Project):
    def __init__(self, position):
        super().__init__(position)
        self.Pxls = (self.Img).load()

    def Apply(self):
        for j in range(self.Img.size[1]):
            for i in range(self.Img.size[0]):
                self.Pxls[i, j] = (int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3), int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3), int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3))
        self.show_image()

class Paste_X(Project):
    def __init__(self, position):
        super().__init__(position)
    def Paste(self,filename2):
        self.Img2 = Image.open(filename2).convert('RGB')  
        self._size1 = [(self.Img).width,(self.Img).height]
        print((self.Img).width)
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (self._size2[0]+self._size1[0],max(self._size2[1],self._size1[1])))

        (self.background).paste(self.Img,(0,0))
        (self.background).paste(self.Img2,(self._size1[0]+1,0))
        (self.background).show()

class Paste_Y(Project):
    def __init__(self, position):
        super().__init__(position)
    def Paste(self,filename2):
        self.Img2 = Image.open(filename2).convert('RGB')  
        self._size1 = [(self.Img).width,(self.Img).height]
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (max(self._size2[0],self._size1[0]), self._size2[1]+self._size1[1]))

        (self.background).paste(self.Img,(0,0))
        (self.background).paste(self.Img2,(0,self._size1[1]+1))
        (self.background).show()

exit=0
Dir=Directory()
while (exit==0):
    entry=""
    entry=input(f"\nWelcome to Pillow Image editor, please select one of the following commands:\n-To start a project, type 0\n-To work on an existing project, type 1\n-To show an image from a project, type 2\n-To close the editor, type END\n")
    if (entry=="END" or entry=="End" or entry=="end"):
        exit=1
    
    elif (entry=="0"):
        pexit=0
        position=0
        pname=input("Please enter the name you will give to your new project (it must be unique): ")
        pfile=input("Please enter the path of the picture you want to edit: ")

        Im = Image.open(pfile).convert('RGB') ##Para que no sobreescriva todo el rato las imagenes de base
        Im.save(f'Edited_{pfile}')

        Dir.New_project(pname, f'Edited_{pfile}')
        position=Dir.Dict["Project"].index(pname)
    
    elif (entry=="1"):
        if (len(Dir.Dict["Project"])==0):
            print("There are no projects available, please create a new one at the menu\n")
            continue
        
        elif (len(Dir.Dict["Project"])!=0):
            position=0
            pexit=0
            print("\nThe projects that are available are: ")
            for i in range (0, len(Dir.Dict["Project"])):
                print(f"-{i}: ",end="")
                print(Dir.Dict["Project"][i])
            position=int(input("Please select a project to open by entering its index number: "))
    elif (entry=="2"):
        if (len(Dir.Dict["Project"])==0):
            print("There are no projects yet\n")
            continue
        
        elif (len(Dir.Dict["Project"])!=0):
            position=0
            pexit=0
            print("\nThe projects that are available are: ")
            for i in range (0, len(Dir.Dict["Project"])):
                print(f"-{i}: ",end="")
                print(Dir.Dict["Project"][i])
            position=int(input("Please select a project to show by entering its index number: "))
            print("Loading picture...")
            Display=Project(position)
            Display.show_image()



                


    if ((entry=="0"or entry=="1")and 0<=position<len(Dir.Dict["Project"])):
        while (pexit==0):
            efile=Dir.Dict["File"][position]
            edit=input(f"\nPlease select what do you want to do to {efile}:\n-To draw a line select 0\n-To pixelate select 1\n-To fuse it with another image select 2\n-To apply grayscale to the image select 3\n-To paste another image select 4\n-To leave this project type END\n")
            if (edit=="end" or edit=="END" or edit=="End"):
                pexit=1
            elif (edit=="0"):
                ImgDrawn = Draw_line(position)
                ImgDrawn.Apply()
                ImgDrawn.Img.save(Dir.Dict["File"][position])
                Dir.Change("Drawn_line", Dir.Dict["File"][position], position)

            elif (edit=="1"):
                Pxl =int(input("Insert pixel amount\n"))
                ImgPixelated = Pixeleado(position, Pxl)
                ImgPixelated.Apply()
                ImgPixelated.Img.save(Dir.Dict["File"][position])
                Dir.Change("Pixelated", Dir.Dict["File"][position], position)

            elif (edit=="2"):
                file2 = input("Insert path for the second image:\n")
                ImgFused = Fuse(position, file2)
                ImgFused.Apply()
                ImgFused.Img.save(Dir.Dict["File"][position])
                Dir.Change("Fused", Dir.Dict["File"][position], position)
            
            elif (edit=="3"):
                ImgGrayScaled = GrayScale(position)
                ImgGrayScaled.Apply()
                ImgGrayScaled.Img.save(Dir.Dict["File"][position])
                Dir.Change("Gray_scaled", Dir.Dict["File"][position], position)
            
            elif(edit=="4"):
                file2 = input("Insert path for the second image:\n")
                choice = input("Type 1 to paste on under, type 2 to paste on the side\n")
                if(choice == "1"):
                    ImgPastedY = Paste_Y(position)
                    ImgPastedY.Paste(file2)
                elif(choice == "2"):
                    ImgPastedX = Paste_X(position)
                    ImgPastedX.Paste(file2)
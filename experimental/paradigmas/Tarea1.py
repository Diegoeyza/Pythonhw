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

    
    def _print(self):
        print(self.Dict)



class Project:
    def __init__(self, filename):
        self.Img = Image.open(filename).convert('RGB')
        self.Img.save(f'Modificado_{filename}')
        self.Img = Image.open(f'Modificado_{filename}').convert('RGB')
        self.filename = filename
    
    def show_image(self):
        self.Img.show()

class Draw_line(Project):
    def __init__(self, filename):
        super().__init__(filename)
    
    def Drawing(self):
        Draw = ImageDraw.Draw(self.Img)
        Draw.line((0,0) + self.Img.size, fill=(200, 000, 200), width=10)
        self.Img.show()
        self.Img.save(f'Modificado_{self.filename}')

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
        Dir.New_project(pname,pfile)
        position=Dir.Dict["Project"].index(pname)
    
    elif (entry=="1"):
        if (len(Dir.Dict["Project"])==0):
            print("There are no projects available, please create a new one at the menu\n")
            pexit=1
        
        elif (len(Dir.Dict["Project"])!=0):
            position=0
            pexit=0
            print("\nThe projects that are available are: ")
            for i in range (0, len(Dir.Dict["Project"])):
                print(f"-{i}: ",end="")
                print(Dir.Dict["Project"][i])
            position=int(input("Please select a project to open by entering its index number: "))

                


    if ((entry=="0"or entry=="1")and 0<=position<len(Dir.Dict["Project"])):
        while (pexit==0):
            s=Dir.Dict["File"][position]
            edit=input(f"\nPlease select what do you want to do to {s}:\n-To Pixelate select 0\n-To xxxxx select 1\n-To fuse it with another image select 2\n-To leave this project type END\n")
            if (edit=="end" or edit=="END" or edit=="End"):
                pexit=1

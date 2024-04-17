from PIL import Image
from Filters import Filter, Pixelate, GrayScale, Draw_line, Draw_circle, Write_text, Resize, Negative, Highlight
from Compositions import Paste_Left, Paste_Right, Paste_Below, Paste_Over, Fuse
from Database import FileCheck, JsonCheck, Directory

Dir=Directory()
class Menu():
    def __init__(self):
        self.exit="0"
        self.entry=""

    def Start(self,dictionary):
        while(self.exit=="0"):
            self.entry=input(f"\nWelcome to Pillow Image editor, please select one of the following commands:\n-To start a project, type 0\n-To work on an existing project, type 1\n-To show an image from a project, type 2\n-To save a project, type 3\n-To open a previously saved project, type 4\n-To show the changes on a project, type 5\n-To undo changes on a project, type 6\n-To close the editor, type END\n")
            if (self.entry=="END" or self.entry=="End" or self.entry=="end"):
                self.exit=1


            elif (self.entry=="6"):
                if (len(dictionary["Project"])==0):
                    print("There are no projects available\n")
                    continue
                
                elif (len(dictionary["Project"])!=0):
                    self.position=0
                    self.pexit=0
                    print("\nThe projects that are available are: ")
                    for i in range (0, len(dictionary["Project"])):
                        print(f"-{i}: ",end="")
                        print(dictionary["Project"][i]+" --> "+dictionary["File"][i])
                    self.position=int(input("Please select the project that you wish to modify: "))
                    self.changes=(Dir.Dict["Changes"][self.position]).split("/")
                    print(f"The changes made to {Dir.Dict['File']} are:")
                    for i in range (0,len(self.changes)-1):
                        print(f"{i}-{self.changes[i]}")
                    self.load=input("Please select the index number of a change to undo all of the changes up to that point or type BACK to return to the menu: ")
                    if (self.load=="BACK" or self.load=="back" or self.load=="Back"):
                        continue
                    elif (self.load)=="0":
                        Im = Image.open(Dir.Dict["Checkpoint"][self.position]).convert('RGB')
                        Im.save(dictionary["File"][self.position])                  


            
            elif (self.entry=="0"):
                self.pexit=0
                self.position=0
                pname=input("Please enter the name you will give to your new project (it must be unique): ")
                self.pfile=FileCheck(input("Please enter the path of the picture you want to edit: "))

                Im = Image.open(self.pfile).convert('RGB')
                Im.save(f'{pname}_Edited_{self.pfile}')

                Dir.New_project(pname, f'{pname}_Edited_{self.pfile}', self.pfile)
                self.position=dictionary["Project"].index(pname)
            
            elif (self.entry=="1"):
                if (len(dictionary["Project"])==0):
                    print("There are no projects available, please create a new one at the menu\n")
                    continue
                
                elif (len(dictionary["Project"])!=0):
                    self.position=0
                    self.pexit=0
                    print("\nThe projects that are available are: ")
                    for i in range (0, len(dictionary["Project"])):
                        print(f"-{i}: ",end="")
                        print(dictionary["Project"][i]+" --> "+dictionary["File"][i])
                    self.position=int(input("Please select a project to open by entering its index number: "))
            
            elif (self.entry=="2"):
                if (len(dictionary["Project"])==0):
                    print("There are no projects yet\n")
                    continue
                elif (len(dictionary["Project"])!=0):
                        self.position=0
                        self.pexit=0
                        print("\nThe projects that are available are: ")
                        for i in range (0, len(dictionary["Project"])):
                            print(f"-{i}: ",end="")
                            print(dictionary["Project"][i]+" --> "+dictionary["File"][i])
                        self.position=int(input("Please select a project to show by entering its index number: "))
                        print("Loading image...")
                        Display=Filter(self.position,dictionary["File"])
                        Display.show_image()

            elif(self.entry=="3"):
                if (len(dictionary["Project"])==0):
                    print("There are no projects yet\n")
                    continue
                else:
                    print("\nThe projects that can be saved are: ")
                    for i in range (0, len(dictionary["Project"])):
                        print(f"-{i}: ",end="")
                        print(dictionary["Project"][i]+" --> "+dictionary["File"][i])
                    Project_position = int(input("Please select a project to save by entering its index number: "))
                    Dir.Save_file(Project_position)

            elif(self.entry=="4"):
                File_to_load = JsonCheck(input("Please select the path of the project to load: "))
                Dir.Open_file(File_to_load)

            if ((self.entry=="0"or self.entry=="1") and 0<=self.position<len(dictionary["Project"])):
                while (self.pexit==0):
                    efile=dictionary["File"][self.position]
                    self.edit=input(f"\nPlease select what do you want to do to {efile}:\n-To draw select 0\n-To pixelate select 1\n-To fuse it with another image select 2\n-To apply grayscale to the image select 3\n-To paste another image select 4\n-To apply a negative filter select 5\n-To apply highlight select 6\n-To rezise image select 7\n-To leave this project type BACK\n")
                    if (self.edit=="BACK" or self.edit=="back" or self.edit=="Back"):
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
                            ImgDrawn = Draw_line(self.position, dictionary["File"])
                            ImgDrawn.Apply(Color)
                            ImgDrawn.Img.save(dictionary["File"][self.position])
                            Dir.Change(f"Drawn_line; {Color}", dictionary["File"][self.position], self.position)

                        elif (choice == "2"):
                            ImgCircle = Draw_circle(self.position, dictionary["File"])
                            ImgCircle.show_size()
                            print("Select x and y coordinate (From upper left corner)")
                            Imgx = int(input("x: "))
                            Imgy = int(input("y: "))
                            Size = int(input("Select size in pixels\n"))
                            
                            ImgCircle.Apply(Imgx, Imgy, Size, Color)
                            ImgCircle.Img.save(dictionary["File"][self.position])
                            Dir.Change(f"Circle; {Imgx}; {Imgy}; {Size}; {Color}", dictionary["File"][self.position], self.position)
                        elif (choice == "3"):
                            ImgWrite = Write_text(self.position, dictionary["File"])
                            ImgWrite.show_size()
                            print("Select x and y coordinate (From upper left corner)")
                            Imgx = int(input("x: "))
                            Imgy = int(input("y: "))
                            Size = int(input("Select size\n"))
                            text = input("Type in text to be used\n")
                            ImgWrite.Apply(Imgx, Imgy, text, Size, Color)
                            ImgWrite.Img.save(dictionary["File"][self.position])
                            Dir.Change(f"Text; {Imgx}; {Imgy}; {text}; {Size}; {Color}", dictionary["File"][self.position], self.position)

                    elif (self.edit=="1"):
                        Pxl =int(input("Insert pixel amount\n"))
                        ImgPixelated = Pixelate(self.position, Pxl, dictionary["File"])
                        ImgPixelated.Apply()
                        ImgPixelated.Img.save(dictionary["File"][self.position])
                        Dir.Change(f"Pixelated; {Pxl}", dictionary["File"][self.position], self.position)

                    elif (self.edit=="2"):
                        file2 = FileCheck(input("Insert path for the second image:\n"))
                        ImgFused = Fuse(self.position, file2, dictionary["File"])
                        ImgFused.Apply()
                        ImgFused.Img.save(dictionary["File"][self.position])
                        Dir.Change(f"Fused; {file2}", dictionary["File"][self.position], self.position)
                    
                    elif (self.edit=="3"):
                        ImgGrayScaled = GrayScale(self.position, dictionary["File"])
                        ImgGrayScaled.Apply()
                        ImgGrayScaled.Img.save(dictionary["File"][self.position])
                        Dir.Change("Gray_scaled", dictionary["File"][self.position], self.position)
                    
                    elif(self.edit=="4"):
                        file2 = FileCheck(input("Insert path for the second image:\n"))
                        choice = input("-Type 1 to paste it under\n-Type 2 to paste it over\n-Type 3 to paste it to the right\n-Type 4 to paste it to the left\n")
                        if(choice == "1"):
                            ImgPastedY = Paste_Below(self.position, dictionary["File"])
                            ImgPastedY.Paste(file2)
                            ImgPastedY.Img.save(dictionary["File"][self.position])
                            Dir.Change(f"Pasted_Below; {file2}", dictionary["File"][self.position], self.position)
                        if(choice == "2"):
                            ImgPastedY = Paste_Over(self.position, dictionary["File"])
                            ImgPastedY.Paste(file2)
                            ImgPastedY.Img.save(dictionary["File"][self.position])
                            Dir.Change(f"Pasted_Over; {file2}", dictionary["File"][self.position], self.position)
                        elif(choice == "3"):
                            ImgPastedX = Paste_Right(self.position, dictionary["File"])
                            ImgPastedX.Paste(file2)
                            ImgPastedX.Img.save(dictionary["File"][self.position])
                            Dir.Change(f"Pasted_Right; {file2}", dictionary["File"][self.position], self.position)
                        elif(choice == "4"):
                            ImgPastedX = Paste_Left(self.position, dictionary["File"])
                            ImgPastedX.Paste(file2)
                            ImgPastedX.Img.save(dictionary["File"][self.position])
                            Dir.Change(f"Pasted_Left; {file2}", dictionary["File"][self.position], self.position)
                        else:
                            print("Invalid input")

                    elif(self.edit=="5"):
                        ImgNegative = Negative(self.position, dictionary["File"])
                        ImgNegative.Apply()
                        ImgNegative.Img.save(dictionary["File"][self.position])
                        Dir.Change(f"Negative", dictionary["File"][self.position], self.position)
                    
                    elif(self.edit=="6"):
                        ValueR = int(input("Insert R (0-255): "))
                        ValueG = int(input("Insert G (0-255): "))
                        ValueB = int(input("Insert B (0-255): "))
                        Tolerance = int(input("Insert a tolerance (0-255): "))

                        ImgHighlight = Highlight(self.position, ValueR, ValueG, ValueB, Tolerance, dictionary["File"])
                        ImgHighlight.Apply()
                        ImgHighlight.Img.save(dictionary["File"][self.position])
                        Dir.Change(f"Highlight; {ValueR}; {ValueG}; {ValueB}; {Tolerance}", dictionary["File"][self.position], self.position)
                    elif(self.edit=="7"):
                        ImgResize = Resize(self.position, dictionary["File"])
                        ImgResize.show_size()
                        Width = int(input("Width: "))
                        Height = int(input("Height: "))
                        ImgResize.Apply(Width, Height)
                        ImgResize.Img.save(dictionary["File"][self.position])
                        Dir.Change(f"Resize; {Width}; {Height}", dictionary["File"][self.position], self.position)

            elif (self.entry=="5"):
                if (len(dictionary["Project"])==0):
                    print("There are no projects available\n")
                    continue
                
                elif (len(dictionary["Project"])!=0):
                    self.position=0
                    self.pexit=0
                    print("\nThe projects that are available are: ")
                    for i in range (0, len(dictionary["Project"])):
                        print(f"-{i}: ",end="")
                        print(dictionary["Project"][i]+" --> "+dictionary["File"][i])
                    self.position=int(input("Please select a project to check its changelog by selecting its index number: "))
                    self.changes=(Dir.Dict["Changes"][self.position]).split("/")
                    print(f"The changes made to {Dir.Dict['File']} are:")
                    for i in range (1,len(self.changes)-1):
                        print(f"{i}-{self.changes[i]}")
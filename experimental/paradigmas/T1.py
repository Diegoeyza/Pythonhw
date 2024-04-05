class Directory:
    def __init__(self):
        self.Dict={"Project":[],"File":[],"Changes":[],"Checkpoint":[]}


    def New_project(self,name,file):
        (self.Dict["Project"]).append(name)
        (self.Dict["File"]).append(file)
        (self.Dict["Checkpoint"]).append(file)
        (self.Dict["Changes"]).append("Changes:")


    
    def Change(self, change, file,position):
        (self.Dict["Checkpoint"])[position]=(self.Dict["File"])[position]
        (self.Dict["File"])[position]=file
        (self.Dict["Changes"])[position]+=f" {change}/ "  #escribe el cambio hecho en cuestión

    
    def print(self):
        print(self.Dict)

diccionario=Directory()
diccionario.New_project("proyecto1","caca.jpeg")
diccionario.Change("Pixelated","yo.jpg",0)
diccionario.print()

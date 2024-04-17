import json
from PIL import Image

class Directory:
    def __init__(self):
        self.Dict={"Project":[],"File":[],"Changes":[],"Checkpoint":[]}
        self.position=0


    def New_project(self, name, file, original_file):
        (self.Dict["Project"]).append(name)
        (self.Dict["File"]).append(file)
        (self.Dict["Checkpoint"]).append(original_file)
        (self.Dict["Changes"]).append("Base Image/")
    

    def Change(self, change, file, position):
        (self.Dict["File"])[position]=file
        (self.Dict["Changes"])[position]+=f"{change}/"

    def Empty_changes(self,position):
        (self.Dict["Changes"][position])="Base Image/"

    
    def Save_file(self, Project_position):
        Im = Image.open(self.Dict["File"][Project_position]).convert('RGB')
        Im.save(f'Saved_{self.Dict["File"][Project_position]}')
        Im.close()
        Saved_dict = {"Project": self.Dict["Project"][Project_position], "File": f'Saved_{self.Dict["File"][Project_position]}',"Changes": self.Dict["Changes"][Project_position],"Checkpoint": self.Dict["Checkpoint"][Project_position]}
        with open(f"Saved_{Saved_dict['Project']}","w") as sf:
            json.dump(Saved_dict, sf)
        print("Save successful")
    
    def Open_file(self, Saved_dict):
        with open(Saved_dict, "r") as lf:
            New_dict = json.load(lf)
        (self.Dict["Project"]).append(New_dict["Project"])
        (self.Dict["File"]).append(New_dict["File"])
        (self.Dict["Checkpoint"]).append(New_dict["Checkpoint"])
        (self.Dict["Changes"]).append(New_dict["Changes"])
        print("Load successful")

    def _print(self):
        print(self.Dict)
from folderpath import FileOrganizer as fo
from pathlib import Path
if __name__ == "__main__":
    print(Path.cwd())
    #try:
    file = input("Type the path of the file here: ")
    filey = fo(file)
    if file == None:
        print("please input an actual file")
    if filey.correctpath():
        filey.checkfiles()
    else:
        print("please type the name of an existing directory")
    
    
from folderpath import *
if __name__ == "__main__":
    curpath()
    #try:
    file = input("Type the path of the file here: ")
    if file == None:
        print("please input an actual file")
    fpath = folderpath(file)
    if correctpath(file):
        checkfiles(fpath)
    else:
        print("please type the name of an existing directory")
    
    
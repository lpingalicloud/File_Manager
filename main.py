from folderpath import *
if __name__ == "__main__":
    curpath()
    file = input("Type the path of the file here: ")
    fpath = folderpath(file)
    print("hello. file manager here")
    print(fpath)
    checkfiles(fpath)
    
from pathlib import Path
import shutil
import os
def folderpath(path):
    #takes folderpath as input and changes it to the correct format for python code
    pathy=Path(path)
    return(pathy)
def curpath():
    print(Path.cwd())

def changeroot(path):
    current = Path.cwd()
    os.chdir(path)
def changehome():
    home = Path.home()
    os.chdir(home)
    print(f"current directory is at the home directory{home}")
def correctpath(path):
    p=Path(path)
    return p.is_dir()
def docsort(name,p):
    if(name.suffix == ".txt" or name.suffix == ".docx" or name.suffix == ".pdf"):
        try:
            os.mkdir(p/"Docs")
            os.chdir(p)
            shutil.move(name,'Docs')
            
        except FileExistsError:
            shutil.move(name,p/'Docs')
        except PermissionError:
            shutil.move(p,'Docs')
def picsort(name,p):
    if(name.suffix == ".jpg" or name.suffix == ".png" or name.suffix == ".jpeg"):
        try:
            os.mkdir(p/"Pics")
            os.chdir(p)
            shutil.move(name,'Pics')
            
        except FileExistsError:
            shutil.move(name,p/'Pics')
        except PermissionError:
            shutil.move(p,'Pics')
def codesort(name,p):
    if(name.suffix == ".py" or name.suffix == ".c" or name.suffix == ".json"):
        try:
            os.mkdir(p/'Code')
            os.chdir(p)
            shutil.move(name,'Code')
            
        except FileExistsError:
            shutil.move(name,p/'Code')
        except PermissionError:
            shutil.move(p,'Code')

def nonesort(name,p):
    if(name.suffix == None):
        try:
            os.mkdir(p/"Nope")
            os.chdir(p)
            shutil.move(name,'Nope')
            
        except FileExistsError:
            shutil.move(name,p/'Nope')
        except PermissionError:
            shutil.move(p,'Nope')


def checkfiles(path):
    p=Path(path)
    for name in p.glob('*'):
        docsort(name,p)
        picsort(name, p)
        codesort(name,p)
        nonesort(name,p)

                
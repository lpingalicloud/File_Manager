from pathlib import Path
import shutil
import os
class FileOrganizer():
    def __init__(self, path):
        self.path = Path(path)
    def curpath(self):
        print(Path.cwd())
        os.chdir(self.path)
    def changehome(self):
        home = Path.home()
        os.chdir(home)
        print(f"current directory is at the home directory{home}")
    def correctpath(self):
        p=Path(self.path)
        return p.is_dir()
    def docsort(self, name):
        #p = os.chdir(self.path)
        p=self.path
        if(name.suffix == ".txt" or name.suffix == ".docx" or name.suffix == ".pdf" or name.suffix == ".md"):
            try:
                os.mkdir(p/"Docs")
                shutil.move(name,p/'Docs')
                
            except FileExistsError:
                shutil.move(name,p/'Docs')

    def picsort(self,name):
        #p = os.chdir(self.path)
        p=self.path
        if(name.suffix == ".jpg" or name.suffix == ".png" or name.suffix == ".jpeg"):
            try:
                os.mkdir(p/"Pics")
                shutil.move(name,p/'Pics')
            
            except FileExistsError:
                shutil.move(name,p/'Pics')
    def codesort(self,name):
        #p = os.chdir(self.path)
        p=self.path
        if(name.suffix == ".py" or name.suffix == ".c" or name.suffix == ".json"):
            try:
                os.mkdir(p/'Code')
                shutil.move(name,p/'Code')
                
            except FileExistsError:
                shutil.move(name,p/'Code')

    def nonesort(self,name):
        #p = os.chdir(self.path)
        p=self.path
        if(name.suffix == ""):
            if name.is_dir():
                return None
            else:
                try:
                    os.mkdir(p/"Nope")
                    shutil.move(name,p/'Nope')
                    
                except FileExistsError:
                    shutil.move(name,p/'Nope')


    def checkfiles(self):
        p = self.path
        for name in p.glob('*'):
            self.nonesort(name)
            self.docsort(name)
            self.codesort(name)
            self.picsort(name)
            
            

                
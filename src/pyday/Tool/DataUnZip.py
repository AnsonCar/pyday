import os
from .unzip import unzip
from ..basic.BasisDay import BasisDay

class DataUnZip(BasisDay):
    def __init__(self):
        super().__init__("unzip")
    
    def inFile(self):
        self.loadDir( [self.inPath] )
        
    def toFile(self):
        self.run()
        
    # 用toFile統一接口，同時提供多個接口方便下自己（我怕忘記）
    def run(self):
        self.loadDir( [self.toPath, self.inPath] )
        files = os.listdir(self.inPath)
        for file in files:
            if file == ".DS_Store":
                continue
            print(f"正在解壓縮{file}...", end=" ")
            unzip(f"{self.inPath}/{file}", self.toPath)
            print("\tDone")
import os
import sys
import pandas as pd

from ..basic import config

class DataReader:
    def __init__(self, inFile=None):
        self.fileName = inFile
        self.inPath = os.path.join( config.worKdir, "pydayData/Reader" )
        self.toPath = os.path.join( config.worKdir, "pydayDist/Reader" )
        self.df = None

        if not "ipykernel" in sys.modules:
            self.loadDir()
            
        if isinstance(inFile, str):
            self.inFile(inFile)
        else:
            self.df = pd.DataFrame(inFile)

    def loadDir(self):
        for path in [self.inPath, self.toPath]:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
    
    def inFile(self, inFile):
        inFileFormat = os.path.splitext(inFile)[-1][1:].lower()
        inFile = os.path.join(self.inPath, inFile)
        if os.path.exists(inFile):
            if inFileFormat == "csv":
                self.df = pd.read_csv(inFile)
            elif inFileFormat == "json":
                self.df = pd.read_json(inFile)
            elif inFileFormat == "xlsx":
                self.df = pd.read_excel(inFile)
            else:
                print( f"input: Does not support '{inFileFormat}' format" )
        else:
            print( f"Did Not Have File: {inFile}" )

    def setPath(self, inPath):
        if not os.path.exists(inPath):
            os.mkdir(inPath)
        self.inPath = inPath

    def getToPath(self):
        return self.toPath

    def toFile(self, toFile):
        toFileFormat = os.path.splitext(toFile)[-1][1:].lower()
        toFile = os.path.splitext(toFile)[0]
        out = f"{self.getToPath()}/{toFile}"
        if toFileFormat == "all":
            self.df.to_csv( f"{out}.csv", index=False)
            self.df.to_json( f"{out}.json" )
            self.df.to_excel( f"{out}.xlsx" )
        elif toFileFormat == "csv":
            self.df.to_csv( f"{out}.csv", index=False)
        elif toFileFormat == "json":
            self.df.to_json( f"{out}.json")
        elif toFileFormat == "xlsx":
            self.df.to_excel( f"{out}.xlsx", index=False)
        else:
            print( "output: Does not support" )

    def setToPath(self, toPath):
        if not os.path.exists(toPath):
            os.mkdir(toPath)
        self.toPath = toPath
import os
import sys
import pandas as pd

from ..basic import config
from ..basic.BasisDay import BasisDay

class DataReader(BasisDay):
    def __init__(self, inFile=None):
        super().__init__("reader")
        self.fileName = inFile
        self.df = None
        
        if isinstance(inFile, str):
            self.inFile(inFile)
        else:
            self.df = pd.DataFrame(inFile)
    
    def inFile(self, inFile):
        self.loadDir( [self.inPath] )
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

    def toFile(self, toFile):
        self.loadDir( [self.toPath] )
        toFileFormat = os.path.splitext(toFile)[-1][1:].lower()
        toFile = os.path.splitext(toFile)[0]
        out = f"{self.toPath}/{toFile}"
        if toFileFormat == "all":
            self.df.to_csv( f"{out}.csv", index=False)
            self.df.to_json( f"{out}.json")
            self.df.to_excel( f"{out}.xlsx" )
        elif toFileFormat == "csv":
            self.df.to_csv( f"{out}.csv", index=False)
        elif toFileFormat == "json":
            self.df.to_json( f"{out}.json")
        elif toFileFormat == "xlsx":
            self.df.to_excel( f"{out}.xlsx", index=False)
        else:
            print( "output: Does not support" )
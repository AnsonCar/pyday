import sys
sys.path.append('..')
from ..basic import config
# import sqlite3
import pandas as pd

class DataReader:
    # constructor
    def __init__(self, inFile=None):
        # Data Memder
        # Basic & Path
        self.fileName = inFile
        self.inPath = None
        self.toPath = None
        
        self.setPath( config.worKdir + "/pydayData" )
        self.setToPath( config.worKdir + "/pydayDist" )
        
    def setPath(self, inFile):
        pass
    
    def getPath(self, toFile):
        pass
    
    def setToPath(self, ):
        pass

    def getToPath(self, ):
        pass
    
    
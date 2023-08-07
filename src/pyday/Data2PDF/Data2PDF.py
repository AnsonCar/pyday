import sys
sys.path.append('..')
import os
import json
from . import BasicStyle
from ..basic import config
from ..ChangLanguage import *
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    PageBreak,
    Image,
    TableStyle,
    Table,
)
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor, black

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.colors import HexColor

styles = getSampleStyleSheet()

class Data2PDF:
    # constructor
    def __init__(self, inFile=None):
        # Data Memder
        # Basic & Path
        self.fileName = inFile
        self.inData = { "data": [ [ "Title_TC", "Did Not Have Data" ] ] }
        self.inPath = None
        self.inImgPath = None
        self.toPath = None
        self.pdf = None
        
        self.setPath( config.worKdir + "/pydayData" )
        self.setImgPath( config.worKdir + "/pydayData/img/" )
        self.setToPath( config.worKdir + "/pydayDist" )
    
        if type(inFile) == str:
            self.inFile(inFile)
        elif type(inFile) == dict:
            self.inData = inFile

        # Style
        self.textStyle = {}
        self.imgStyle = {}
        self.tableStyle = {}
        
        # Text
        for style in BasicStyle.Text:
            self.addText(style)
            
        # for style in BasicStyle.Image:
        #     pass
        
        for style in BasicStyle.Table:
            pass
        
    # mothed
    # input
    def inFile(self, inFile):
        inFile = f"{self.inPath}/{inFile}"
        with open(inFile, "r") as file:
            self.inData = json.loads(file.read())

    def setPath(self, path): 
        # 如果沒有此路徑會自動生成 If the path does not exist, the directory will be created
        if not os.path.exists(path):
            os.mkdir(path)
        self.inPath = path

    def getPath(self):
        return self.inPath

    def setImgPath(self,path):
        self.inImgPath = path
    
    def getImgPath(self):
        return self.inImgPath
    
    # output
    def toFile(self, toFile, footer=True, cl=None):
        self.pdf = SimpleDocTemplate(
            f"{self.getToPath()}/{toFile}",
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72,
        )
        
        data = []
        for line in self.inData["data"]:
            data.append( self.toStyle( line ) )
            
        if footer:
            # 如果需要在 PDF 頁面底部添加頁碼，則設置 onFirstPage 和 onLaterPages 參數，並生成 PDF 文件。
            self.pdf.build(data, onFirstPage=self.infooter, onLaterPages=self.infooter)
        else:
            self.pdf.build(data)

    def setToPath(self, path):
        # 如果沒有此路徑會自動生成 If the path does not exist, the directory will be created
        if not os.path.exists(path):
            os.mkdir(path)
        self.toPath = path

    def getToPath(self):
        return self.toPath
    
    def toStyle(self, line):
        if line[0] == "img":
            return self.inImg( line[1] )
        elif line[0] == "table":
            return self.inTable( line[1] )
        else:
            return self.inText( line[1], line[0] )
        
    # stlye
    # font
    def addFont(self):
        pass
    
    def getFont(self):
        pass
    
    # Text
    def inText(self, data, style):
        return  Paragraph( data, self.textStyle[ style ] )
    
    def addText(self, style):
        # 檢查是否為 list
        if type(style[0]) == list and type(style[1]) == list:
            # 檢查是否多於一個名稱和字體，以及名稱字體數目是否相同
            if len(style[0]) == len(style[1]) :
                for num in range(len(style[0])):
                    self.setTextStyle( len(style), style, style[0][num], style[1][num] )
        else:
            self.setTextStyle( len(style), style, style[0], style[1])

    def setTextStyle(self, num, style, textName, fontName ):
        if num == 5:
            self.textStyle[textName] = ParagraphStyle( "styleNormalCustom",fontName=fontName, parent=styles["Normal"], alignment=style[2],fontSize=style[3],leading=style[4] )
        elif num == 6:
            self.textStyle[textName] = ParagraphStyle( "styleNormalCustom",fontName=fontName, parent=styles["Normal"], alignment=style[2],fontSize=style[3],leading=style[4], leftIndent=style[5] )
        elif num == 7:
            self.textStyle[textName] = ParagraphStyle( "styleNormalCustom",fontName=fontName, parent=styles["Normal"], alignment=style[2],fontSize=style[3],leading=style[4], leftIndent=style[5], textColor=HexColor( style[6] ) )

    def getTextStyle(self):
        Text = [ f"{num+1:4d} {i}" for num, i in enumerate(self.textStyle.keys()) ]
        return "\nText Style:\n\n" + "\n".join(Text) + "\n"
    
    # img
    def inImg(self, img, img_width, img_height):
        return Image(img, width=img_width, height=img_height)
    
    def addImg(self):
        self.imgStyle = 1
    
    # def getImg():
    #     pass
    
    # table
    def inTable( ):
        pass
    
    def setTable():
        pass
    
    # def getTable():
    #     pass
    
    ## footer 在 PDF 頁面底部寫入頁碼
    def infooter(self, canvas, doc):
        canvas.saveState()
        canvas.drawString(doc.width + doc.rightMargin, 20, f"{doc.page}")
        canvas.restoreState()
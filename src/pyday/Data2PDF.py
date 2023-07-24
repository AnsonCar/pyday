import json
from .basic import config
from .basic import BaseClass

#
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Image

# 字體
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 樣式
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

# 寫入字體
for name, path in config.font_ttf.items():
    pdfmetrics.registerFont(TTFont(name, path))
# 設定字體
styles = getSampleStyleSheet()
# 標題
Tile_TC = Regular_TC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_TC_Bold",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontSize=18,
    leading=22,
)
# 副標題
SubTile_TC = Regular_TC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_TC_Bold",
    parent=styles["Normal"],
    alignment=TA_LEFT,
    fontSize=16,
    leading=20,
)
# 內文（一般/基礎）
Basis_TC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_TC_Regular",
    parent=styles["Normal"],
    alignment=TA_LEFT,
    fontSize=12,
    leading=18,
)


class Data2PDF:
    def __init__(self, fileName, outfile, footer=True):
        self.fileName = fileName
        self.fileFormat = fileName.split(".")[-1]
        self.pdf = SimpleDocTemplate(
            f"{outfile}.pdf",
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72,
        )
        self.data = self.inFile(fileName)
        self.footer = footer
        self.toFile()

    # setter
    def inFile(self, file):
        data = []
        if self.fileFormat == "json":
            with open(self.fileName, "r") as fileJson:
                json_str = json.loads(fileJson.read())
            for line in json_str["data"]:
                if line[0] == "img":
                    set = self.inImg(line[1])
                else:
                    set = self.inText(line)
                data.append(set)

        else:
            with open(file, "r") as file:
                for line in file.read().split():
                    data.append(Paragraph(line, Basis_TC))
        return data

    def inText(self, data):
        if data[0] == "Title":
            return Paragraph(data[1], Tile_TC)

        elif data[0] == "SubTitle":
            return Paragraph(data[1], SubTile_TC)
        else:
            return Paragraph(data[1], Basis_TC)

    def inImg(self, img):
        img_reader = ImageReader(img)
        img_width, img_height = img_reader.getSize()
        max_width, max_height = self.pdf.width + 72, self.pdf.height + 72
        if img_width > max_width or img_height > max_height:
            ratio = min(max_width / img_width, max_height / img_height)
            img_width *= ratio
            img_height *= ratio
        return Image(
            img,
            width=img_width,
            height=img_height,
        )

    # 寫入頁碼
    def setfooter(self, canvas, doc):
        canvas.saveState()
        canvas.drawString(doc.width + doc.rightMargin, 20, f"{doc.page}")
        canvas.restoreState()

    # getter
    def toFile(self):
        if self.footer:
            self.pdf.build(
                self.data, onFirstPage=self.setfooter, onLaterPages=self.setfooter
            )
        else:
            self.pdf.build(self.data)


# https://ithelp.ithome.com.tw/articles/10236883

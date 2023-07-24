from .basic import config
from .basic import BaseClass

#
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

# 設定字體
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 寫入字體
for name, path in config.font_ttf.items():
    pdfmetrics.registerFont(TTFont(name, path))

# 
styles = getSampleStyleSheet()
Regular_TC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_TC_Regular",
    parent=styles["Normal"],
)

Regular_SC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_SC_Regular",
    parent=styles["Normal"],
)

class Data2PDF:
    def __init__(self, file, fileName):
        self.pdf = SimpleDocTemplate(
            f"{fileName}.pdf", pagesize=letter
        )  # , leftMargin=12, rightMargin=12, topMargin=12, bottomMargin=12
        self.data = self.inFile(file)
        self.toFile()

    # setter
    # 輸入 數據文件
    def inFile(self, file):
        data = []
        with open(file, "r") as file:
            for line in file.read().split():
                data.append(Paragraph(line, Regular_SC))
        return data

    # getter
    # 輸出 數據文件
    def toFile(self):
        self.pdf.build(self.data)

# https://ithelp.ithome.com.tw/articles/10236883
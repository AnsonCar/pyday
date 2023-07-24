import os
import json
from .basic import config
from .basic import BaseClass
# 樣式
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
# 字體
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
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
# 內文（一般/基礎)
Basis_TC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_TC_Regular",
    parent=styles["Normal"],
    alignment=TA_LEFT,
    fontSize=12,
    leading=18,
)


class Data2PDF:
    def __init__(self, fileName, outfile, img_path=None, footer=True):
        """
        初始化方法，用於設置 PDF 文檔的基本參數。

        :param fileName: str, 要轉換為 PDF 的數據文件名。
        :param outfile: str, 轉換後的 PDF 文件名。
        :param footer: bool, 是否在 PDF 頁面底部添加頁碼。預設為 True。
        """
        # 設置文件名、文件格式、PDF 文檔參數等屬性
        self.img_path = img_path if img_path else ""
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
        # 轉換數據，生成 PDF 文檔
        self.toFile()

    # setter
    def inFile(self, file):
        """
        用於讀取數據文件，並轉換為 PDF 中可用的格式。

        :param file: str, 數據文件名。
        :return: list, 轉換後的數據列表。
        """
        data = []
        if self.fileFormat == "json":
            # 如果數據文件格式為 JSON，則讀取 JSON 文件。
            with open(self.fileName, "r") as fileJson:
                json_str = json.loads(fileJson.read())
            # 將 JSON 中的數據轉換為 PDF 中可用的格式，並添加到數據列表中。
            for line in json_str["data"]:
                if line[0] == "img":
                    set = self.inImg(line[1])
                else:
                    set = self.inText(line)
                data.append(set)

        else:
            # 如果數據文件格式不是 JSON，則直接讀取文本文件。
            with open(file, "r") as file:
                for line in file.read().split():
                    data.append(Paragraph(line, Basis_TC))
        return data

    def inText(self, data):
        """
        將文本數據轉換為 PDF 中可用的段落格式。

        :param data: list, 要轉換的文本數據。
:return: Paragraph, 轉換後的段落對象。
        """
        if data[0] == "Title":
            # 如果是標題，則使用 Tile_TC 樣式創建段落對象。
            return Paragraph(data[1], Tile_TC)

        elif data[0] == "SubTitle":
            # 如果是副標題，則使用 SubTile_TC 樣式創建段落對象。
            return Paragraph(data[1], SubTile_TC)
        else:
            # 如果是內文，則使用 Basis_TC 樣式創建段落對象。
            return Paragraph(data[1], Basis_TC)

    def inImg(self, img):
        """
        將圖片數據轉換為 PDF 中可用的圖像對象。

        :param img: str, 要轉換的圖片文件名。
        :return: Image, 轉換後的圖像對象。
        """
        img = os.path.join(self.img_path,img)
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
        """
        在 PDF 頁面底部寫入頁碼。

        :param canvas: Canvas, PDF 頁面畫布對象。
        :param doc: SimpleDocTemplate, PDF 文檔對象。
        """
        canvas.saveState()
        canvas.drawString(doc.width + doc.rightMargin, 20, f"{doc.page}")
        canvas.restoreState()

    # getter
    def toFile(self):
        """
        將數據轉換為 PDF 文件。
        """
        if self.footer:
            # 如果需要在 PDF 頁面底部添加頁碼，則設置 onFirstPage 和 onLaterPages 參數，並生成 PDF 文件。
            self.pdf.build(
                self.data, onFirstPage=self.setfooter, onLaterPages=self.setfooter
            )
        else:
            # 如果不需要在 PDF 頁面底部添加頁碼，則直接生成 PDF 文件。
            self.pdf.build(self.data)

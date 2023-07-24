import os
import json
from .basic import config
from .basic import BaseClass

# 樣式
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    PageBreak,
    Image,
    TableStyle,
    Table,
)
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.colors import HexColor, black

# 字體
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 寫入字體
for name, path in config.font_ttf.items():
    pdfmetrics.registerFont(TTFont(name, path))
# 設定字體
styles = getSampleStyleSheet()
# 標題
Tile_TC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_TC_Bold",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontSize=18,
    leading=24,
    # textColor=HexColor("#4f71bd")
)
# 副標題
SubTile_TC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_TC_Bold",
    parent=styles["Normal"],
    alignment=TA_LEFT,
    fontSize=16,
    leading=22,
)
# 副標題2
SubTile2_TC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_TC_Bold",
    parent=styles["Normal"],
    alignment=TA_LEFT,
    fontSize=16,
    leading=22,
    leftIndent=16 * 2,
)
# 內文（一般/基礎)
Basis_TC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_TC_Regular",
    parent=styles["Normal"],
    alignment=TA_LEFT,
    fontSize=12,
    leading=20,
)
# 內文2（一般/基礎)
Basis2_TC = ParagraphStyle(
    "styleNormalCustom",
    fontName="Noto_Sans_TC_Regular",
    parent=styles["Normal"],
    alignment=TA_LEFT,
    fontSize=12,
    leading=20,
    leftIndent=16 * 2,
)


class Data2PDF:
    def __init__(self, fileName, outfile, img_path=None, footer=True):
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
        data = []
        if self.fileFormat == "json":
            # 如果數據文件格式為 JSON，則讀取 JSON 文件。
            with open(self.fileName, "r") as fileJson:
                json_str = json.loads(fileJson.read())
            # 將 JSON 中的數據轉換為 PDF 中可用的格式，並添加到數據列表中。
            for line in json_str["data"]:
                if line[0] == "img":
                    set = self.inImg(line[1])
                elif line[0].lower() == "table":
                    set = self.inTable(line)
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
        if data[0].lower() == "title":
            # 如果是標題，則使用 Tile_TC 樣式創建段落對象。
            return Paragraph(data[1], Tile_TC)

        elif data[0].lower() == "subtitle":
            # 如果是副標題，則使用 SubTile_TC 樣式創建段落對象。
            return Paragraph(data[1], SubTile_TC)
        elif data[0].lower() == "subtitle2":
            # 如果是副標題2，則使用 SubTile2_TC 樣式創建段落對象。
            return Paragraph(data[1], SubTile2_TC)
        elif data[0].lower() == "text":
            # 如果是副標題2，則使用 SubTile2_TC 樣式創建段落對象。
            return Paragraph(data[1], Basis_TC)
        elif data[0].lower() == "text2":
            # 如果是內文，則使用 Basis_TC 樣式創建段落對象。
            return Paragraph(data[1], Basis2_TC)

    def inImg(self, img):
        img = os.path.join(self.img_path, img)
        img_reader = ImageReader(img)
        img_width, img_height = img_reader.getSize()
        max_width, max_height = self.pdf.width, self.pdf.height
        if img_width > max_width or img_height > max_height:
            ratio = min(max_width / img_width, max_height / img_height)
            img_width *= ratio
            img_height *= ratio
        return Image(
            img,
            width=img_width,
            height=img_height,
        )

    def inTable(self, data):
        tableStyle = TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # 置中對齊
                ("FONTNAME", (0, 0), (-1, -1), "Noto_Sans_TC_Regular"),  # 字體
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # 上下置中
                ("GRID", (0, 0), (-1, -1), 0.5, black),  # 框線黑色，寬度0.5
            ]
        )
        return Table(
            data[1],
            style=tableStyle,
            colWidths=self.pdf.width / len(data[1][0]),
            spaceBefore=12,
            spaceAfter=12,
        )

    # 寫入頁碼
    def infooter(self, canvas, doc):
        # 在 PDF 頁面底部寫入頁碼
        canvas.saveState()
        canvas.drawString(doc.width + doc.rightMargin, 20, f"{doc.page}")
        canvas.restoreState()

    # getter
    def toFile(self):
        # 將數據轉換為 PDF 文件。
        if self.footer:
            # 如果需要在 PDF 頁面底部添加頁碼，則設置 onFirstPage 和 onLaterPages 參數，並生成 PDF 文件。
            self.pdf.build(
                self.data, onFirstPage=self.infooter, onLaterPages=self.infooter
            )
        else:
            # 如果不需要在 PDF 頁面底部添加頁碼，則直接生成 PDF 文件。
            self.pdf.build(self.data)


# https://ithelp.ithome.com.tw/articles/10239020
# https://docs.reportlab.com/reportlab/userguide/ch7_tables/

# 這是 ReportLab 中 Table 類別的建構式（constructor）的參數說明：

# data：必要參數，要顯示在表格中的資料，格式為二維的列表或元組。
# colWidths：一個列表，包含每個欄位的寬度（以 point 為單位，1 inch = 72 points）。如果沒有指定，則根據內容自動調整欄位寬度。
# rowHeights：一個列表，包含每個列的高度（以 point 為單位）。如果沒有指定，則根據內容自動調整列高度。
# style：一個 TableStyle 物件，包含表格的樣式設置（如文字對齊、框線顏色等）。
# splitByRow：一個布林值或整數。如果是 True 或 1，表示當表格太長無法顯示在當前頁面時，自動將表格拆分成多個子表格，並顯示在多個頁面上。如果是 False 或 0，表示整個表格只顯示在一頁中，而超出頁面的部分會被切割掉。也可以指定要拆分的行數。
# repeatRows：一個整數，表示在每個新頁面上是否要重複顯示表格的前幾行。預設值為 0，表示不重複顯示。
# repeatCols：一個整數，表示在每個新頁面上是否要重複顯示表格的前幾列。預設值為 0，表示不重複顯示。
# rowSplitRange：一個元組，表示每個子表格中要顯示的行數範圍。例如，如果 rowSplitRange=(0, 2)，表示每個子表格只顯示前 2 行。
# spaceBefore：一個浮點數，表示表格上方的空白間距（以 point 為單位）。
# spaceAfter：一個浮點數，表示表格下方的空白間距（以 point 為單位）。
# cornerRadii：一個元組，表示表格的四個角的半徑（以 point 為單位，順序為左上、右上、右下、左下）。預設值為 None，表示不設置圓角。

import config
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib.pagesizes import letter

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

# 寫入字體
for name, path in config.font_ttf.items():
    pdfmetrics.registerFont(TTFont(name, path))
    
# 拿預設的樣式
styles = getSampleStyleSheet()
styleNormalCustom = ParagraphStyle(
    'styleNormalCustom',
    fontName='Noto_Sans_TC_Regular',
    parent=styles["Normal"],
)

fileName = "example.pdf"
pdfTemplate = SimpleDocTemplate(fileName)
story = []
story.append(Paragraph("Hello World"))
story.append(Paragraph("你好世界111", styleNormalCustom))
pdfTemplate.build(story)

# class toPDF:
#     def __init__(self, name):
#         pdf = SimpleDocTemplate(f'{name}.pdf', pagesize=A4, leftMargin=12, rightMargin=12, topMargin=12, bottomMargin=12)
#         # pdf.setFont("", 16)

# https://ithelp.ithome.com.tw/articles/10236883
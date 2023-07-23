from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

class toPDF:
    def __init__(self, name):
        __pdf = SimpleDocTemplate(f'{name}.pdf', pagesize=A4, leftMargin=12, rightMargin=12, topMargin=12, bottomMargin=12)
        
# https://ithelp.ithome.com.tw/articles/10236883
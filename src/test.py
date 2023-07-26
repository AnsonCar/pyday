from pyday import DataReader
# from pyday import DataVis
from pyday import Data2PDF
from pyday import ChangLang

d2pdf = Data2PDF("test.json")
d2pdf.toFile("test.pdf")

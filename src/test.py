# from pyday import DataReader
# dr = DataReader()
# dr.inFile("train.csv")
# dr.toFile("test.all")

from pyday import Data2PDF
d2pdf = Data2PDF()
d2pdf.inFile("test.json")
print( d2pdf.getTableStyle() )
# d2pdf.toFile("test2.pdf") 
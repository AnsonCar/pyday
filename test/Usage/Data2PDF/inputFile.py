import sys
sys.path.append('/Users/ansoncar/Desktop/MyProject/pyday/src/')

# 建構實例 - 初始化
# 第一種，不帶參數。使用inFile()引入需要讀取的文件。
from pyday import Data2PDF
d2pdf = Data2PDF()
d2pdf.inFile("test.json") 

# 第二種，帶有參數。初始化同時引入需要讀取的文件。
from pyday import Data2PDF
d2pdf = Data2PDF("test.json")
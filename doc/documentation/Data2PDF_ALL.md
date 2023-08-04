# Data2PDF 指令大全
## 基本
```python
from pyday import Data2PDF
# 構建實例
d2pdf = Data2PDF()
d2pdf = Data2PDF("test.json")
# 引入文件
d2pdf.inFile("test.json")
# 查看引入文件目錄
d2pdf.getPath()
d2pdf.getImgPath()
# 改變引入文件目錄
d2pdf.setPath() # 如果沒有此路徑會自動生成
d2pdf.setImgPath() # 如果沒有此路徑會自動生成

# 輸出文件
d2pdf.toFile("test.pdf")
depdf.toFile("test.pdf", footer=True, cl=None)
# 查看輸出文件目錄
d2pdf.getToPath()
# 改變輸出文件目錄
d2pdf.setToPath() #如果沒有此路徑會自動生成
```

## 設定樣式
### 字體 Font
```python

```

### 文字 Text
```python
# 內部使用
self.inText(data, textStyle)
# 加入字體樣式
# [ [名字], [字體], 對齊方法, 字體大小, 行距, 左縮排, 文字顏色 ]
# TA_LEFT = 0, TA_CENTER = 1, TA_RIGHT = 2, TA_JUSTIFY = 4
textStyle ＝ [ [ "Text_TC", "Text_SC" ], [ "Noto_Sans_TC_Bold", "Noto_Sans_SC_Bold "], 0, 12, 20, 16, "#FFFFFF" ]
d2pdf.addTextStyle( textStyle )
# 查看字體樣式
d2pdf.getTextStyle()
```

### 圖片 Image
```python

```

### 頁碼 footer
```python
# 內部使用
self.infooter()
```

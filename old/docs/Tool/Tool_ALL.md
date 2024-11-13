# Tool 工具箱 指令大全
## ChangLang
> 基於 opencc 及 googletrans

### 䌓簡轉換
```python
from pyday import ChangLang
text = "歡迎使用pyday的ChangLang䌓簡轉換功能"
cl = ChangLang(text)
print(cl.sc) # 繁轉簡體
print(cl.tc) # 轉為繁體
```

```python
from pyday import ChangLang
text = "歡迎使用pyday的ChangLang䌓簡轉換功能"
cl = ChangLang()
cl.setData(text)
print(cl.sc) # 繁轉簡體
print(cl.tc) # 轉為繁體
```

### 中文翻釋成英文 （需連網）
```python
from pyday import ChangLang
cl = ChangLang()
text = "歡迎使用pyday"
print(cl.en2tc(text))
```

### 英文翻釋成中文（需連網）
```python
from pyday import ChangLang
cl = ChangLang()
text = "Data Science and Analytics"
print(cl.en2tc(text))
```

---

## dirTree 文件樹狀結構

```python
from pyday import dirTree
import os
path = os.getcwd() # 取得當前目錄
exclude_list = [".DS_Store", ".git", "node_modules", "__pycache__"] # 不想顯示的文件
dirTree(path, exclude_list, maxlevel=1) # maxlevel 最大顯示層數
```

## unzip 解壓縮文件
```python
from pyday import unzip
filepath = "yourPath/fileName.zip"
savepath = "yourPath"
unzip(filepath, savepath)
```

## DataUnZip 批量解壓縮文件
```python
# 默認解壓縮的文件放入 pydayData/unzip
# 默認會在 pydayDist/unzip 生成解壓縮文件
from pyday import DataUnZip
dup = DataUnZip().run()
# dup = DataUnZip().toFile()
```
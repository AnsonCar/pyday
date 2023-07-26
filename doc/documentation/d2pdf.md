# Data2PDF
Data2PDF 是基於pandas開發的，用於處理二維數據。
## input / output
接受兩種初始化方法"：
第一種，不帶參數。使用inFile()引入需要讀取的文件。
```python
rd = DataReader()
re.inFile("test.csv")
```
第二種，帶有參數。初始化同時引入需要讀取的文件。
```python
rd = DataReader("test.csv")
```

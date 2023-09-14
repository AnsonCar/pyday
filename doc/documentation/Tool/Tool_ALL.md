# Tool 工具箱 指令大全
## ChangLang

```python

```

```python
from pyday import ChangLang
text = "歡迎使用pyday"
cl = ChangLang(text)
print(cl)
```

## dirTree 文件樹狀結構
```python
from pyday import dirTree
import os
path = os.getcwd()
exclude_list = [".DS_Store", ".git", "node_modules", "__pycache__"]
dirTree(path, exclude_list, maxlevel=1)
```

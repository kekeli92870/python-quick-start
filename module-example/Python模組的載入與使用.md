## 關於Python Module 模組的載入與使用
> 獨立的程式檔案   
> 將程式寫在一個檔案中，此檔案可重複載入使用    
> 先載入模組，再使用模組中的函式或變數

### 基本語法
**載入模組**
```python
import 模組名稱

import 模組名稱 as 模組別名
```
**使用模組**
```python
模組名稱或別名.函式名稱(參數資料)

模組名稱或別名.變數名稱
```

### 內建模組
**sys模組** 取得系統相關資訊
```python
# 載入sys模組
import sys
#import sys as s

# 使用sys模組
print(sys.platform)  # 印出作業系統
#print(s.platform)
print(sys.maxsize)   # 印出整數型態的最大值
#print(s.maxsize)
print(sys.path)      # 印出搜尋模組的路徑
#print(s.path)
```

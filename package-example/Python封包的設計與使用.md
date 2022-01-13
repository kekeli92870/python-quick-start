## 關於 Python Package 封包的設計與使用

> 用來整理丶分類模組程式

#### 專案檔案配置
* 專案資料夾
  * 主程式.py         (`main.py`)
  * 封包資料夾        (geometry)
    * _ _init__.py  (`__init__.py` 特殊的Python程式)
    * 模組一.py      (`line.py`)
    * 模組二.py.     (`point.py`)

#### 基本語法
```python
import 封包名稱.模組名稱

import 封包名稱.模組名稱 as 模組別名
```

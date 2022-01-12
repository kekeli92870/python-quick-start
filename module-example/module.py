# 載入內建的 sys 模組並取得資訊
import sys
print(sys.platform)
print(sys.maxsize)

import sys as s
print(s.platform)
print(s.maxsize)

# 建立自訂模組
# 建立 geometry 模組,載入使用
"""
import geometry
result= geometry.distance(1,1,5,5)
print(result) # 印出 5.656854249492381
result=geometry.slope(1,2,5,6)
print(result) # 印出 1.0
"""

#調整搜尋模組的路徑
import sys
sys.path.append("modules") # 在模組的搜尋路徑列表中[新增路徑]
print(sys.path) # 印出模組的搜尋路徑列表
print("---------------------")
import geometry
print(geometry.distance(1,1,5,5)) # 印出 5.656854249492381

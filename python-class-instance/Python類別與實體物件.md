## Python 類別的定義與使用 - Class Attributes
> 封裝的變數或函式，統稱 *類別的屬性*  
> 要先定義類別，才能使用類別中封裝的屬性
### 基本語法
#### 定義類別
```python
class 類別名稱：
    定義封裝的變數
    定義封裝的函式

# 範例：定義 Test類別
class Test:
    x=3 #定義變數
    def say(): #定義函式
        print("Hello World")
```
#### 使用類別
```python
類別名稱.屬性名稱

# 範例：使用 Test類別
Test.x+3   #取得屬性 x的資料
Test.say() #呼叫屬性 say函式
```

## Python 實體物件的建立與使用 - 實體屬性 Instance Attributes
> 封裝在實體物件中的變數  
> 使用類別建立實體物件並操作實體屬性  
### 基本語法
#### 建立實體
```python
class 類別名稱：
    #定義初始化函式
    def __init__(self):
      透過操作 self 來定義實體屬性
#建立實體物件，放入變數obj中
obj=類別名稱() #呼叫初始化函式

# 範例一：
class Point:
    def __init__(self):
      self.x=3
      self.y=4
#建立實體物件，此實體物件包含 x 和 y 兩個實體屬性
p=Point()

# 範例二：
class Point:
    def __init__(self, x, y):
      self.x=x
      self.y=y
#建立實體物件，建立時可直接傳入參數資料
p=Point(1,5)
```

#### 使用實體
```python
實體物件.實體屬性名稱

# 範例：
class Point:
    def __init__(self, x, y):
      self.x=x
      self.y=y
#建立實體物件，並取得實體屬性資料
p=Point(1,5)
print(p.x+p.y) #印出 6
```

## Python 實體物件的建立與使用 - 實體方法 Instance Methods
> 封裝在實體物件中的函式
### 基本語法
#### 建立方法
```python
class 類別名稱：
    #定義初始化函式
    def __init__(self):
      定義實體屬性
    定義實體方法/函式
#建立實體物件，放入變數obj中
obj=類別名稱() 

class 類別名稱：
    #定義初始化函式
    def __init__(self):
      封裝在實體物件中的變數
    def 方法名稱(self, 更多自訂參數)
      方法主體, 透過 self 操作實體物件
#建立實體物件，放入變數obj中
obj=類別名稱()
```
#### 使用方法
```python
實體物件.實體方法名稱(參數資料)

# 範例： 
class Point:
    def __init__(self, x, y):
      self.x=x
      self.y=y
    def show(self):
      print(self.x, self.y)

p=Point(1,5) #建立實體物件
p.show()     #呼叫實體方法
```
      
      

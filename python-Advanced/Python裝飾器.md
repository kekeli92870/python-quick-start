## 關於Python 裝飾器 Decorator
> 裝飾器： 特殊設計的函式，用來**輔助**其他的函式  
> 裝飾器本質上是一個函式

### 基本裝飾器
#### 定義裝飾器
```python
def 裝飾器名稱(回呼函式名稱):
    def 內部函式名稱():
        #撰寫裝飾器內部的程式碼
        回呼函式名稱()
    return 內部函式名稱
```
#### 使用裝飾器
```python
@裝飾器名稱
def 函式名稱():
    #函式內部的程式碼
函式名稱() #呼叫帶有裝飾器的函式
```
##### 範例
```python
def testDecorator(callback):
    def innerFunc():
        print("裝飾器")
        callback()
    return innerFunc
    
@testDecorator
def decoratedFunc():
    print("普通函式")

decoratedFunc() #先印出 裝飾器，再印出 普通函式
```
```python
def testDecorator(callback):
    def innerFunc():
        print("裝飾器")
        callback(3)
    return innerFunc
    
@testDecorator
def decoratedFunc(data):
    print("普通函式",data)

decoratedFunc() #先印出 裝飾器，再印出 普通函式 3
```

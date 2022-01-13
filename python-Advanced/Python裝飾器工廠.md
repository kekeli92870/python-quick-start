## 關於Python 裝飾器工廠 Decorator Factory
> 裝飾器工廠： 用來 **生產** 裝飾器的函式

#### 定義裝飾器工廠
```python
def 裝飾器工廠名稱(參數名稱,...):
    def 裝飾器名稱(回呼函式名稱)：
        def 內部函式名稱():
            #裝飾器內部的程式碼
            回呼函式名稱()
        return 內部函式名稱
    return 裝飾器名稱
```
#### 使用裝飾器工廠
```python
@裝飾器工廠名稱(參數資料,...)
def 函式名稱():
    #函式內部的程式碼
函式名稱() #呼叫帶有裝飾器的函式
```
##### 範例
```python
def testFactory(base):
    def testDecorator(callback):
        def innerFunc():
            print("裝飾器",base)
            callback()
        return innerFunc
    return testDecorator

@testFactory(3)
def decoratedFunc():
    print("普通函式")

decoratedFunc() #印出 裝飾器 3,再印出 普通函式
```
```python
def testFactory(base):
    def testDecorator(callback):
        def innerFunc():
            result=base*3
            callback(result)
        return innerFunc
    return testDecorator

@testFactory(3)
def decoratedFunc(result):
    print("普通函式",result)

decoratedFunc() #印出 普通函式 9
```

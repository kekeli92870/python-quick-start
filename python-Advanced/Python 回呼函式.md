## 關於Python 回呼函式 Callback Function
> 回呼函式： 透過參數傳遞函式到另一個函式中

#### 基礎的函式參數
```python
# 範例一：
def test(arg):
    print(arg)
    
#呼叫 test，傳遞參數
test(3)
test("Hello World")
```
```python
# 範例二：
def test(arg):
    print(arg)
#建立另一個函式 handle
def handle():
    print(100)
#呼叫 test，傳遞參數
test(handle)
```

#### 回呼函式
```python
# 範例一：
def test(arg):
    arg() #呼叫回呼函式
    
def handle():
    print(100)

test(handle)
```
```python
# 範例二：
def test(arg):
    arg(50) #回呼函式的參數
    
def handle(data):
    print(data) #印出 50

test(handle)
```

## 關於Python 生成器 Generator 基礎使用
> 生成器： 動態產生可疊代的資料，搭配 for迴圈使用

#### 建立生成器
> 使用 **yield** 語法： 在函式中使用 **yield** 語法，呼叫時回傳生成器

##### 基本語法
```python
yield 資料
```
```python
def 函式名稱():
    yield 資料
    
#呼叫函式，回傳生成器
變數名稱＝函式名稱()

# 範例：
def test():
    yield 3
#呼叫函式，回傳生成器
gen=test()
print(gen)
```

#### 搭配 for迴圈使用
##### 語法
```python
for 變數名稱 in 生成器:
    將生成器產生的資料，逐一取出
```
```python
# 範例一：
def test():
    yield 3
#呼叫函式，回傳生成器
gen=test()
#搭配 for迴圈使用，印出 3 
for d in gen:
    print(d)

# 範例二：
def test():
    yield 3
    yield 5
#呼叫函式，回傳生成器
gen=test()
#搭配 for迴圈使用，逐一印出 3 和 5
for d in gen:
    print(d)
```

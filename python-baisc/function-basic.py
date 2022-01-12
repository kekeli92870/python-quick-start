# 定義函式
# 函式內部的程式碼,若沒有被呼叫,就不會執行
def multiply():
    print(3*4)

def multiply2(n1,n2):
    print(n1*n2)
    #return #return 10

def multiply3(n1,n2):
    print(n1*n2)
    return n1*n2

def multiply4(n1,n2):    
    return n1*n2

# 呼叫函式
multiply()
multiply()
multiply2(10,2)
multiply2(8,2)

value=multiply2(2,1)
print(value) # 印出 None

value2=multiply3(3,4)
print(value2)

value3=multiply4(3,4)+multiply4(10,5)
print(value3)

# 程式的包裝
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum+=n
    print(sum) # 印出 1+..+n 的結果

calculate(10) # 印出 55
calculate(20) # 印出 210

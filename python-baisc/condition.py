# 判斷式
if True:
    print("True 執行")

if False:
    print("True 執行")
else:
    print("False 執行")

x=input("請輸入數字: ") # 取得字串形式的使用者輸入
x=int(x) # 將字串型態轉換成數字型態
if x>100:
    print("大於 100")
else:
    print("小於等於 100")
 
y=input("請輸入數字: ") 
y=int(y)
if y>200:
    print("大於 200")
elif y>100:
    print("大於 100 小於等於 200")
else:
    print("小於等於 100")

# 四則運算
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
op=input("請輸入運算: +, -, *, / : ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)    
else:
    print("請輸入正確的運算..")
# 參數的預設資料
"""def power(base,exp):
    print(base**exp)"""

def power(base,exp=0):
    print(base**exp)
power(3,2) # 印出 9
power(4) # 印出 1

# 使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(2,4) # 印出 0.5
divide(n2=2,n1=4) # 印出 2.0

# 無限參數資料
"""
def avg(*nums): # nums 會是一個 Touple
    print(nums)
avg(3,4) # 印出 (3,4)
avg(3,5,10) # 印出 (3,5,10)
avg(1,4,-1,-8) # 印出 (1,4,-1,-8)
"""
"""
def avg(*nums):
    for n in nums:
        print(n)
avg(3,4) # 印出 3 4
"""
def avg(*nums): 
    #print(nums)
    sum=0
    for n in nums:
        sum+=n
        #print(n)
    print(sum/len(nums))
avg(3,4) # 印出 3.5
avg(3,5,10) # 印出 6.0
avg(1,4,-1,-8) # 印出 -1.0

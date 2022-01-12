# while迴圈
""" # 無窮迴圈
n=1
while True:
    print(n)
    n+=1
"""
n=1
while n<=3:
    print(n) # 印出 1 2 3
    n+=1

# 等差級數 1+2+3+...+10 = ?
n=1
sum=0 # 記錄累加的結果
while n<=10:
    sum=sum+n
    n+=1
print(sum) # 印出 55
    
# for迴圈
for x in [3,5,1]:
    print(x) # 印出 3 5 1

for y in "Hello":
    print(y) # 印出 H e l l o

for z in range(5):
    print(z) # 印出 0 1 2 3 4

for z in range(5,10):
    print(z) # 印出 5 6 7 8 9

# 等差級數 1+2+3+...+10 = ?
sum=0
for x in range(1,11):
    sum+=x
print(sum)

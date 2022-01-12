# 有序可變動列表 List
grades=[45,60,55,70,90]
print(grades)
print(grades[0]) # 印出 45
print(grades[3]) # 印出 70
grades[0]=15 # 把15放到列表中的第一個位置
print(grades) # 印出 [15,60,55,70,90]
print(grades[1:4]) # 印出 [60,55,70]
grades[1:4]=[] # 連續刪除列表中從編號 1 到編號 4(不包括)的資料
print(grades) # 印出 [15,90]
grades=[15,60,55,70,90]
grades=grades+[12,33] # 列表的串接
print(grades) # 印出 [15,60,55,70,90,12,33]
# 取得列表的長度 
# len(列表資料)
length=len(grades) 
print(length) 
# 巢狀列表
data=[[3,4,5],[6,7,8]]
print(data[0]) # 印出 [3,4,5]
print(data[0][0]) # 印出 [3]
print(data[0][1]) # 印出 [4]
print(data[0][0:2]) # 印出 [3,4]
data[0][0:2]=[5,5,5]
print(data[0]) # 印出 [5,5,5,5]
print(data)

# 有序不可變動列表 Tuple
tdata=(3,4,5)
print(tdata[0:2]) # 印出 (3,4)
#tdata[0]=5 # 發生錯誤: Tuple的資料不可以變動
print(tdata)



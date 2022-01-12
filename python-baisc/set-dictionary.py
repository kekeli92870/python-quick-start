# 集合 Set 的運算
s={3,4,5}
print(3 in s) # 印出 Ture
print(10 in s) # 印出 False
print(10 not in s) # 印出 Ture

s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 # 交集: 取2個集合中相同的資料
print(s3) # 印出 {4,5}
s3=s1|s2 # 聯集: 取2個集合中所有的資料,但不重複取
print(s3) # 印出 {3,4,5,6,7}
s3=s1-s2 # 差集: 從 s1 中減掉與 s2 重疊的部份
print(s3) # 印出 {3}
s3=s1^s2 # 反交集: 取2個集合中不重疊的部份
print(s3) # 印出 {3,6,7}

# set(字串) 把字串中的字母拆解成集合
s=set("Hello")
print(s)
print("H" in s)
print("A" in s)

# 字典 Dictionary 的運算
# key-value 的配對
dic={"apple":"蘋果","data":"資料"}
print(dic["apple"]) # 印出 蘋果
dic["apple"]="大蘋果"
print(dic["apple"]) # 印出 大蘋果

dic={"apple":"蘋果","data":"資料"}
# 判斷 key 是否存在
print("apple" in dic)
print("test" in dic)

# 刪除字典中的鍵值對 key-value pair
dic1={"apple":"蘋果","data":"資料"}
print(dic1)
del dic1["apple"]
print(dic1)

# dic={x:x*2 for x in 列表}
# 從列表的資料產生字典
dic2={x:x*2 for x in [3,4,5]}
print(dic2) # 印出 {3:6,4:8,5:10}

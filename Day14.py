#练习
number=[12,5,83,26,47,91,34]
max=number[0]
for i in range(len(number)):
    if max<number[i]:
        max=number[i]
print(max)


#字符串
my_str="itheima and itcast"
a=my_str[8]
print(a)

#字符串的操作
#index
index=my_str.index("and")
print(index)

#replace(将字符串全部替换）
new_my_str=my_str.replace("and","or")
print(new_my_str)

#split(分隔符字符串）
my_str="python itheima and itcast"
list=my_str.split(" ")
print(list)

#strip(去除前后空格）
my_str="12itheima and itcast21"
print(my_str.strip( ))

#统计字符串中某字符串的出现次数
print(my_str.count("a"))

#统计字符串的长度
print(len(my_str))

#字符串的遍历
str="黑马程序员"
index=0
while index<len(str):
    print(str[index])
    index+=1

for i in str:
    print(i)

#练习
str="itheima itcast boxuegu"
print(str.count("it"))
new_str=str.replace(" ","|")
print(new_str)
list=new_str.split("|")
print(list)

#序列
#序列的操作 切片
my_list=[0,1,2,3,4,5]
print(my_list[1:4:1])
my_tuple=(0,1,2,3,4,5)
print(my_tuple[::-1])
my_str="01234567"
print(my_str[ : :2])

#练习
str="学python，来黑马程序员，月薪过万"
new_str=str[::-1]
print(new_str)
print(new_str[::-1][9:14])

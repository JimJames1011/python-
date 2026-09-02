#列表的循环
"""list=[1,2,3,4,5,6,7,8,9,10]
index=0
while index<len(list):
    print(list[index])
    index+=1
for index in list:
    print(list[index])
    index+=1"""

#练习
list=[1,2,3,4,5,6,7,8,9,10]
def while_ou():
    index=0
    list1=[]
    while index<len(list):
        if list[index]%2==0:
            element=list[index]
            list1.append(element)
            index += 1
        else:
            index += 1
    print(list1)
while_ou()


list3=[1,2,3,4,5,6,7,8,9,10]
def for_ou():
    list2=[]
    for index in list3:
        if index%2==0:
            element=list3[index-1]
            list2.append(element)
    print(list2)
for_ou()


#元组
#定义元组
t0=(1,"helo",True)
tuple()#空元组

#定义单个元素的元素
t1=(1,)

#元组的嵌套
t2=((1,2,3),(4,5,6))

#下标索引取出内容
print(t2[1][2])

#元组的操作：index的查找
t3=(1,3,4,"hh",True,75,"jj")
print(t3.index(3))

#元组的统计
t4=(1,2,3,4,5,6,7,8,9,10)
print(t4.count(5))

#元组的元素数量
print(len(t4))

#元组的遍历：whlie
index=0
while index<len(t4):
    print(t4[index])
    index+=1

#元组的遍历：for
for i in t4:
    print(i)

#练习
t=("Jim",19,['music','Lady Gaga'])
print(t.index(19))
name=t[0]
print(name)
del t[2][0]
print(t)
t[2].append("Mariay")
print(t)
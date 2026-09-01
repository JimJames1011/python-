#数据容器
"""name_list=['Jim','James','Jinx','samira','neon']
print(name_list)"""


#list列表
"""name_list=['itheima','iscast','python',666,True]
print(name_list)
x=[[1,2,3],[4,5,6]]
print(x)
y=[name_list,[1,2,3]]
print(y)
print(name_list[0])#正向索引
print(name_list[-1])#反向索引
print(y[0][0])#嵌套列表索引"""


#列表的查询（方法）  index
name_list=['itheima','iscast','python',666,True]
index=name_list.index(True)#查询
print(index)

#修改下标索引值
name_list[0]="Jim"
print(name_list[0])

#在指定位置插入新元素  列表.insert
name_list.insert(0,"Samira")
print(name_list)

#在尾部追加元素  列表.append
name_list.append("James")
print(name_list)

#在尾部追加一批元素  列表.extend
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)

#删除元素  del列表【下标】 列表.pop(下标）
del name_list[0]
print(name_list)
name_list.pop(0)
element=name_list.pop(0)
print(name_list,element)

#删除某元素在列表中的第一个匹配项  列表.remove
list3=[1,2,3,2,3]
list3.remove(3)
print(list3)

#清空列表 列表.clear
name_list.clear()
print(name_list)

#统计某元素在列表内的数量  列表.count（元素）
list4=[1,2,3,1,1,1]
print(list4.count(1))

#统计列表内有多少元素  len（列表）
print(len(list4))


#练习
student_age=[21,25,21,23,22,20]
student_age.append(31)
print(student_age)
student_age.extend([29,33,30])
print(student_age)
element1=student_age.pop(0)
print(student_age,element1)
element2=student_age.pop(-1)
print(student_age,element2)
index=student_age.index(31)
print(index)

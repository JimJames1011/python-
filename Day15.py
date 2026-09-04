#集合{}
my_set={"船只教育","黑马程序员","itheima","船只教育","黑马程序员","itheima"}
print(my_set)

#添加新元素  集合.add()
my_set.add("python")
print(my_set)

#移除元素 集合.remove()
my_set.remove("itheima")
print(my_set)

#随机取出一个元素  集合.pop()
element=my_set.pop()
print(element)
print(my_set)

#清空集合
print(my_set.clear())

#取两个集合的差集  集合1.difference(集合2)
set1={1,3,4,5}
set2={1,2,3,6}
set4=set1.difference(set2)
print(set)

#消除2个集合的差集  集合1.difference_update(集合2)
set1.difference_update(set2)
print(set1)
print(set2)

#两个集合合并 集合1.union(集合2)
set3=set1.union(set2)
print(set3)

#统计集合元素数量len(）
print(len(set3))

#集合的遍历
for element in set3:
    print(element)

#练习
my_list=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
my_set=set()
for element in my_list:
    print(element)
    my_set.add(element)
print(my_set)

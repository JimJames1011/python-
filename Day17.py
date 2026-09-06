#演示数据容器的通用功能
my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_str="abcdefg"
my_set={1,2,3,4,5}
my_dict={"key1":1,"key2":2,"key3":3,"key4":4}

#len元素个数
print(len(my_list))
print(len(my_tuple))
print(len(my_str))
print(len(my_set))
print(len(my_dict))

#max最大元素
print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print(max(my_set))
print(max(my_dict))

#min最小元素
print(min(my_list))
print(min(my_tuple))
print(min(my_str))
print(min(my_set))
print(min(my_dict))

#类型转换：容器转列表
print(list(my_tuple))
print(list(my_str))
print(list(my_set))
print(list(my_dict))

#类型转换：容器转元组
print(tuple(my_list))
print(tuple(my_str))
print(tuple(my_set))
print(tuple(my_dict))

#通用排序功能  sorted(容器，[reverse=True])
a={3,2,4,1}
print(sorted(a))

#abc比较abd
print({'abc'>'abd'})

#a比较ab
print({'a'>'ab'})

#a比较A
print({'a'>'A'})
"""#字典
my_dict={"Jim":19,"James":20,"samira":21}  #不允许key的重复
dict1={}
dict2=dict()

#字典数据的获取
print(my_dict["Jim"])
print(my_dict["James"])
print(my_dict["samira"])

#字典的嵌套
stu_score={"Jim":
               {"math":150,"English":150,"science":150},
           "James":
               {"math":0,"English":15,"science":100},
           "samira":
               {"math":99,"English":10,"science":19}
           }
print(stu_score)
print(stu_score["Jim"]["math"])

#新增元素 字典[Key]=Value
my_dict["neon"]=22
print(my_dict)

#更新元素 字典[Key]=Value
my_dict["Jim"]=60
print(my_dict)

#删除元素  字典.pop(Key)
stu_score.pop("Jim")
print(stu_score)

#清除字典  字典.clear()
print(stu_score.clear())

#获取全部的key 字典.keys()
keys=my_dict.keys()
print(keys)

#遍历字典
for i in my_dict:
    print(i)
    print(my_dict[i])

#统计字典里元素数量
print(len(stu_score))"""

#练习
dict1={'王力宏':{'部门':'科技部','工资':3000,'级别':1},
       '周杰伦':{'部门':'市场部','工资':5000,'级别':2},
       '林俊杰':{'部门':'市场部','工资':7000,'级别':3},
       '张学友':{'部门':'科技部','工资':4000,'级别':1},
       '刘德华':{'部门':'市场部','工资':6000,'级别':2}
}
print(f"全体员工当前信息如下：{dict1}")
for i in dict1:
    if dict1[i]['级别']==1:
        dict1[i]['级别']+=1
        dict1[i]['工资']+=1000
print(f"全体员工级别为1的员工完成升职加薪操作，操作后：{dict1}")
#for循环
"""name ="iitheima"
for x in name:
    print(x)"""

#练习
"""name ="itheima is a brand of itcast"
num=0
for x in name:
    if x == "a":
        num=num+1
print(num)"""

#range语句
"""range(5)
print(list(range(5)))
range(5,10)
print(list(range(5,10)))
range(5,10,2)
print(list(range(5,10,2)))"""

"""for x in range(10):
    print(x)
for x in range(10):
    print("我喜欢你")"""


#练习
"""num=100
i=0
for x in range(1,num):
    if x%2 ==0:
        i+=1
print(f"1到100范围内，有{i}个偶数")"""


#for循环的嵌套
"""for i in range(1,101):
    print(f"今天是给他表白的第{i}天")
    for j in range(10):
        print("送给他一朵玫瑰花")
print(f"第{i}天，表白成功")"""

#练习
"""for i in range(0,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end='')
    print()"""

#练习发工资
money=10000
for i in range(1,20):
    import random
    num = random.randint(1, 10)
    if num<5:
        print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位")
        continue
    else:
        money=money-1000
        print(f"向员工{i}发放工资1000元，账户余额还有{money}元")
        if money==0:
            print("工资发完了，下个月领取吧")
            break
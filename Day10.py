#复习
"""for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i} = {i*j}\t",end='')
    print()"""


"""#函数
name="itheima"
length=len(name)
print(length)
x=0
for i in name:
    x+=1
print(x)
#定义函数
def my_len(data):
    count =0
    for i in data:
        count+=1
    print(count)
my_len(name)"""

"""
def say_hello():
     print("hello")
say_hello()"""


#练习
"""def hanshu():
    print("欢迎来到黑马程序员！")
    print("请出示您的健康码及72小时核酸证明！")
hanshu()"""

#函数的传入参数
"""def add():
    x=int(input("请输入一个数："))
    y=int(input("再输入一个数："))
    print(f"{x+y}")
add()"""

"""def add(x,y):
    print(f"{x+y}")
add(10,20)"""


#练习
"""def cha(x):
    print("欢迎来到黑马程序员！请出示您的健康码及72小时核酸证明,并配合测量体温！")
    if x<=37.5:
        print(f"体温测量中，您的体温是{x}度，体温正常请进！")
    else:
        print(f"体温测量中，您的体温是{x}度，需要隔离！")
cha(38)"""


#函数的返回值
"""def add(x,y):
    result=x+y
    return result
r=add(10,20)
print(r)"""


#None类型
def say_hi():
    print("hi")
result=say_hi()
print(f"无返回值函数，返回的内容是{result}")
print(f"无返回值函数，返回的内容类型是{type(result)}")

#None用于if判断
def chaeck_age(x):
    if x>18:
        return"SuCCESS"
    else:
        return None
result=chaeck_age(28)
if not result:
    print("未成年")
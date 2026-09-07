#函数的多返回值
def return_result():
    return 1,2
x,y=return_result()
print(x,y)

#函数的多种传参方式
#位置参数
def use_info(name,age,gender):
    print(f"your name is {name} and your age is {age} and your gender is {gender}")
use_info("Jim",19,"male")

#关键字参数
use_info(name='Jim',gender='male',age=19)

#缺省参数
def info(name,age,gender='male'):
    print(f"Your name is {name} and your age is {age} and your gender is {gender}")
info('Jim',19)
info('James',20,'female')

#不定长参数
def inf(*agrs):
    print(agrs)
inf('Jim',19,'male','handsome','sophisticated')  #元组

def inform(**kwargs):
    print(kwargs)#要满足k=V
inform(name='Jim',age=19,gender='male')  #字典

#匿名函数
#函数作为参数传递
def test_func(compute):
    result=compute(1,2)
    print(result)

def compute(x,y):
    return x+y
test_func(compute)

#lambda函数（只能临时使用一次）lambda 传入参数：函数体（一行代码）
def test_func2(compute):
    result=compute(2,3)
    print(result)
test_func2(lambda x,y:x+y)

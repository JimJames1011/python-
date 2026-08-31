#复习
"""def introduce(name):
    print(f"my name is {name}")
introduce("Jim")"""


#函数的说明文档
"""def func(x,y):
    func函数可以接收2个参数，进行2个数相加的功能
    :param x: 表示相加的一个数字
    :param y: 表示相加的另一个数字
    :return: 返回值是两个数相加的结果
    result=x+y
    return result"""


#函数的嵌套调用
"""def func_b():
    print("2")
def func_a():
    print("1")
    func_b()
func_a()"""


#局部变量
"""def test_a():
    num=100       #局部变量
    print(num)
test_a()


#全局变量
num=100    #全局变量
def test_b():
    print(num)
def test_c():
    print(num)
test_b()
test_c()"""

#global 关键字
"""def test_a():
    global num
    num=100       #局部变量
    print(num)
test_a()
print(num)"""


#练习
money=5000000
name=input("请输入您的姓名")
def check():
    print(f"{name},您好，您的余额剩余：{money}元")
def deposit():
    global money
    add_money=int(input(f"{name},您好，请输入你的存钱金额："))
    money = add_money+money
    print(f"{name},您好，您的余额剩余：{money}元")
def withdraw():
    global money
    decline_money=int(input(f"{name},您好，请输入你的取钱金额："))
    if decline_money>money:
        print(f"抱歉，您的余额只有{money}元")
    else:money = money-decline_money
    print(f"{name},您好，您的余额剩余：{money}元")
def ATM():
    print(f"{name}，您好，欢迎来到Jim银行ATM，请选择操作")
    print("查询余额 【输入1】\t")
    print("存款    【输入2】\t")
    print("取款    【输入3】\t")
    print("退出    【输入4】\t")
    print()
    while True:
        choice=int(input("请输入您的选择："))
        if choice==1:
            check()
            continue
        elif choice==2:
            deposit()
            continue
        elif choice==3:
            withdraw()
            continue
        else:
            break
ATM()
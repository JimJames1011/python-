"""age=int(input("Enter your age:"))
if age>18:
    print("you are old enough")
else:
    print("you are not old enough")"""

"""#判断语句的嵌套
print("欢迎来到黑马动物园")
if int(input("输入你的身高："))>120:
    print("sorry 你的身高超过120cm不可以免费")
    print("不过如果你的VIP等级超过3还可以免费")
    if int(input("请输入你的VIP等级:"))>3:
        print("恭喜你VIP等级超过3 可以免费游玩")
    else:print("sorry 你需要补票")
else:print("welcome")"""

#练习 and or
"""age=int(input("Enter your age:"))
if age>=18 and age<30:
    if int(input("输入你的入职时间"))>2 or int(input("请输入你的级别："))>3:
        print("你可以领取了")
    else:print("你不可以领取")
else:print("你不可以领取")
"""

#练习 猜数字
import random
num=random.randint(1,10)
num1=int(input("你有三次猜的机会 请猜第一次："))
if num1==num:
    print(f"恭喜你猜中了，结果就是{num}")
else:
    if num1>num:
        print("猜大了")
    else:
        print("猜小了")
    num2=int(input("请猜第二次："))
    if num2==num:
        print(f"恭喜你猜中了，结果就是{num}")
    else:
        if num2>num:
            print("猜大了")
        else:
            print("猜小了")
        num3 = int(input("请猜第三次："))
        if num3==num:
            print(f"恭喜你猜中了，结果就是{num}")
        else:
            print(f"sorry 没有猜对 答案是{num}")
"""age=19
print(age==19)
print(age >19)
print(age>=19)"""

#if语句
"""age=19
if age>=18:
    print("你成年了")
print(f"你现在已经{age}岁了")"""

#练习
"""print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age=int(input("请输入你的年龄："))
if age>=18:
    print("您已成年，游玩需要补票10元")
print("祝您游玩愉快")"""

#if else语句
"""print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age=int(input("请输入你的年龄："))
if age>=18:
    print("您已成年，游玩需要补票10元")
else:
    print("您未成年，可以免费游玩")
print("祝您游玩愉快")"""

#练习
"""print("欢迎来到黑马动物园")
height=int(input("请输入你的身高(cm):"))
if height>120:
    print("您的身高超过120cm，游玩需要购票10元")
else:
    print("您的身高未超过120cm，可以免费游玩")
print("祝您游玩愉快")"""

#elif
"""print("欢迎来到黑马动物园")
height=int(input("请输入你的身高(cm):"))
vip_level=int(input("请输入你的VIP等级"))
if height<120:
    print("您的身高未超过120cm，可以免费游玩")
elif  vip_level>3:
    print("您的VIP等级超过3，可以免费游玩")
else:
    print("不好意思，所有条件都不满足，需要购票10元")
print("祝您游玩愉快")"""

#练习
num=8
if int(input("请输入第一次猜想的数字："))==num:
    print("恭喜猜对了")
elif int(input("不对，再猜一次："))==num:
    print("恭喜猜对了")
elif int(input("不对，再猜最后一次："))==num:
    print("恭喜猜对了")
else: print(f"Sorry,全部猜错啦，我想的是：{num}")
#复习猜数字
"""import random
num = random.randint(1,100)
sum=0
while True:
    sum +=1
    num1 = int(input("请猜："))
    if num1==num:
        print(f"恭喜数字就是{num} 而且你用了{sum}次")
        break
    elif num1>num:
        print("too high")
    elif num1<num:
        print("too low")"""



#break continue
"""while True:
    num=int(input("enter your number:"))
    if num==1:
        break"""


"""num=0
while num<=100:
    num+=1
    if num%2==0:
        continue
    print(num)"""

num=1
sum=0
while num<=100:
    sum+=num
    num+=1
    if num<=100:
        continue
    print(sum)


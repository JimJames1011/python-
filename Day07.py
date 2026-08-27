#循环语句
"""i=0
while i<100:
    print(i)
    i +=1"""

#练习
"""i=1
sum=0
while i<=100:
    sum +=i
    i +=1
    print(sum)"""

#练习猜数字
"""import random
num = random.randint(1,100)
sum=0
while True:
    guess_num = int(input("Guess the number: "))
    sum+=1
    if guess_num==num:
       print(f"猜了{sum}次,数字是{num}")
       break
    elif guess_num>num:
        print("too high")
    elif guess_num<num:
        print("too low")"""

#while嵌套
"""i=1
while i<=100:
    print(f"今天是第{i}天")
    i+=1
    j=0
    while j <=10:
        print(f"送他{j}朵花")
        j+=1
print("我喜欢他")"""

#练习
i=1
while i<=9:
    j = 1
    while j<=i:
      print(f"{j}*{i}={i*j}\t",end='')
      j+=1
    i+=1
    print()
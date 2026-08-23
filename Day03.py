"""name="Jim"
age=19
print(f"My name is {name} and I am {age} years ago")
message="My name is %s"%name
print(message)"""

"""#输入input() 输出print()
name=input("请告诉我你是谁")
print("welcome,%s"%name)
age=int(input("请告诉我你的年龄"))
print("what a %d boy"%age)"""


name=input("请输入你的姓名")
age=int(input("请输入你的年龄"))
height=float(input("请输入你的身高"))
next_age=age+1
print(f"My name is {name},my age is {age} and my height is {height} cm")
print(f"and next year you're {next_age} years old")
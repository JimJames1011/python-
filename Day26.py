#对象
"""class Student:
    name=None
    gender=None
    age=None
    native=None
stu_1=Student()
stu_1.name="Jim"
stu_1.gender="Male"
stu_1.age=19
stu_1.native="China"
print(stu_1.name)
"""

#类的定义和使用、
class Student:
    name=None
    age=None
    def info(self):
        print(f"my name is {self.name} and my age is {self.age}")

stu1=Student()
stu1.name="Jim"
stu1.age=19
stu1.info()


#类和对象
class Clock:
    hours=0
    minutes=0
    def time(self):
        print(f"{self.hours}:{self.minutes}")
clo1=Clock()
clo1.hours=1
clo1.minutes=1
clo1.time()
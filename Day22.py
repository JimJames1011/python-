""""#模块
#[from 模块名]   import[模块|类|变量|函数|*】[as 别名】
import time
print("start to sleep")
time.sleep(5)
print("end sleep")

#导入特定功能
from time import sleep
print("start sleep")
sleep(5)
print("end sleep")

#导入全部功能  from 模块名 import*  功能名（）
from time import*
print("start sleep")
sleep(1)
print("end sleep")

#as定义别名
import time as tt
print(12)
tt.sleep(1)
print(23)
"""
#自定义模块
#新建一个python文件
import my_model1
my_model1.test1(1,2)
#当导入多个模块，且模块内部含有同名功能，那么后面的会覆盖前面的

#main
from my_model1 import test1

#all 变量 当使用from XXX import*时，只能导入该列表的元素
from my_model1 import*
test1(1,2)
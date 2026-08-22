""""#查看类型信息 print直接输出信息
print(type(19))
print(type("jim"))
#使用变量存储type语句的结果
x=type("jim")
print(x)"""

"""#类型转换
#将数字类型转换成字符串
num_str=str(11)
print(type(num_str),num_str)
#将字符串转换成数字类型
num_int=int("11")
print(type(num_int))
#整数转浮点数
float_num=float(11)
print(type(float_num),float_num)"""


#标识符 只能有：英文 中文 数字 下划线（不能用中文 数字不能开头）

"""#运算符+-*/ //（取整除） %（取余） **（指数）
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
#赋值运算符=
c=1+2*3
print(c)
#复合赋值运算符
c=1
c+=1
print(c)
c//=2
print(c)"""

"""#字符串的拼接
name="jim"
age=19
print("My name is:"+name,"age is",age)"""

"""#字符串格式化
personality="handsome boy"
message="Jim is a %s"%personality
print(message)
#%表示占位 s表示把变量变成字符串放入占位的地方
height=185
weight=103
message="Jim's height is %s and his weight is %s"%(height,weight)
print(message)
#%s：将内容转换为字符串 %d：将内容转换为整数 %f：将内容转换为浮点型
name="JM传媒"
set_up_year=2026
stock_price=10000
message="%s成立于%d 其股价为%f"%(name,set_up_year,stock_price)
print(message)"""

"""#数字精度控制m：控制宽度 .n控制小数点精度
num=11.72
print("%7.2f"%num)"""

"""#快速格式化字符串 f“内容{变量}” 这种方式不理会类型 不做精度控制
height=185
weight=103
print(f"my height is {height} and weight is {weight}")"""

"""#对表达式进行格式化
print("1+1=%d"%(1+1))
print(f"1+1={1+1}")"""

#test 股价计算小程序
name="传智播客"
stock_price=19.99
stock_code="003032"
stock_price_daily_growth_factor=1.2
growth_days=7
final_price=stock_price_daily_growth_factor**growth_days*stock_price
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数是：%s，经过%d天的增长后，股价达到了%.2f"%(stock_price_daily_growth_factor,growth_days,final_price))



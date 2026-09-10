#了解异常
#open("D:/abc.txt",UTR=8)

#捕获异常
#try:可能发生错误的代码
try:
    f=open("D:/abc.txt","r")
# except:如果出现异常执行的代码
except:
    print("文件不存在，现在切换写入模式")
    f=open("D:/abc.txt","w")
#捕获指定异常
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')

#捕获多个异常
try:
    1/0
except(NameError,ZeroDivisionError):
    print(ZeroDivisionError)

#未正确设置捕获异常类型，将无法捕获异常
#捕获所有异常
try:
    1 / 0
    print(name)
except:
    print("出现异常了")

#异常else
try:
    print(1)
except:
    print('出现异常了')
else:
    print("我是else，没有异常的时候执行的代码")

#异常的finally
try:
    f=open("D:/abc.txt","r")
except:
    print('出现异常了')
    f=open("D:/abc.txt","w")
else:
    print("nice 没有异常")
finally:
    f.close()

#异常的传递性
def func1():
    print('这是func1的开始')
    num=1/0
    print('这是func1的结束')
def func2():
    print('这是func2的开始')
    func1()
    print('这是func2的结束')
def main():
    try:
        func2()
    except:
        print(1)
main()
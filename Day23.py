#安装第三方包
#科学计算：numpy包
#数据分析：pandas
#大数据计算：pyspark、apache-flink
#图形可视化;matplotib、pyecharts
#人工智能：tensorflow

#安装 提示符程序输入：pip install 包

#练习
def str_reserve(s):
    return s[::-1]  #反转
def substr(s,x,y):
    return s[x:y]
print(str_reserve("abcdefgh"))
def print_file_info(filename):
    f=None
    try:
        f=open(filename,'r',encoding="UTF-8")
        content=f.read()
        print(content)
    except:
        print("File not found")
    finally:
        f.close()
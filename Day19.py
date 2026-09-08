#文件编码

#文件
#打开文件  open(name,mode,encoding)
f=open("D:/test.txt","r",encoding="UTF-8")
print(type(open("D:/test.txt","r",encoding="UTF-8")))

#read()   wenjian
f.read(10)

#readline()一次读取一行
#readlines()读取全部行

#for循环读取文件
for line in f:
    print(line)

#文件的关闭 close()
f.close()

#with open 语法操作文件
with open("D:/test.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line)


#练习
with open("D:/word.txt","r",encoding="UTF-8") as f:
    content=f.read()
    print(content.count("itheima"))

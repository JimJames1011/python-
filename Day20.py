#打开文件
f=open("D:/python.txt","w",encoding="UTF-8")
#文件写入
f.write('hello world')#内容写入到内存中   若文件存在 则清空换成写的东西 不存在则写入
#内容刷新
f.flush() #将内存中积攒的内容，写入到硬盘的文件中
#close关闭
f.close()

#文件的追加
f=open("D:/python.txt","a",encoding="UTF-8")
f.write("HELLO WORLD")
f.close()

#练习
fr=open("D:/python.txt","r",encoding="UTF-8")
fw=open("D:/python.txt","w",encoding="UTF-8")
for line in fr:
    line=line.strip()
    if line.strip(",")[4]=="测试":
        continue
    else:
        fw.write(line)
        fw.write("\n")
fr.close()
fw.close()
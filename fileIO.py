f = open ('/home/dong/文档/ex1.txt','r')
print(f.read())
f.close()

f = open('/home/dong/文档/ex1.txt','a')
f.write('\n你好')
f.close()

with open('/home/dong/文档/ex1.txt','r') as f1:  #推荐用 with open as 的方法操作文件
    print(f1.read())
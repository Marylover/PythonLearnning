from io import StringIO 
f = StringIO()  #把字符串写入StringIO
f.write('hello')
f.write(' ')
f.write('world')

print(f.getvalue())  #getvalue()方法用于获取写入后的字符串

t = StringIO('Life is short\n\nI use python')  #用一个字符串来初始化StringIO
while True:
    s = t.readline() 
    if s == '':  #直到读到一整行的空字符串
        break
    print(s.strip())  #strip() ,移除首尾空格，strip('char'),移除首尾指定字符

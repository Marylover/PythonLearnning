from datetime import datetime
import os

path = os.getcwd()

print('文件名     大小        上次修改')
print ('.....................')

for f in os.listdir(path):
    #name = os.path.basename(f) 不需要这句
    size = os.path.getsize(f)
    time = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')  #获取当前时间且转化为特定格式的字符串
    flag = '/' if os.path.isdir(f) else ''  #如果是文件夹，就在它的后面加'/'
    print('%10d  %s  %s%s' % (size, time, f, flag))
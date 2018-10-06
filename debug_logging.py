import logging 
logging.basicConfig(level = logging.INFO) #这句指定记录信息的级别，有debug,info,warning,error几个级别

s = '0'
n = int(s)
logging.info('n = %d' % n)  #这句输出信息，要与之前设置的级别匹配
print(10/n)


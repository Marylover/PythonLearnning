from functools import reduce
digits  =  {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return digits[s]
def fun(x,y):
    return x*10+y
def str2float(s):
    dot = s.index('.')
    s = s[:dot]+s[dot+1:]
    return reduce(fun,map(char2num,s))/pow(10,len(s)-dot)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
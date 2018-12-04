from functools import reduce

def str2num(s):
    try:    #若该字符串不能转化为整数，就触发异常，并把它转化为浮点数
        return int(s) 
    except ValueError as e:
        return float(s)
def calc(exp):
    ss = exp.split('+')  #返回以'+'为分界的几个字符串，并把它们放入一个列表
    ns = map(str2num, ss) #把他们转化为数字
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10/n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        #raise   #输出 ValueError: invalid value: 0 异常
        raise  ZeroDivisionError('input error') #若 raise带有参数，那么它可将错误类型转化

bar()
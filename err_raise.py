class FooError(ValueError):  #通过继承 ValueError类来自定义自己的错误
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s'%s) #通过if语句的判断抛出异常
    return 10 / n

foo('0')
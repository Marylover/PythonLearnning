def my_abs(x):
    if not isinstance (x,(int,float)):    ##只允许整形和浮点型参数，否则抛出TypeError异常
        raise TypeError('bad operand type')
    if x >=0:
        return x
    else:
        return -x

def _odd_iter(): #定义一个可以生成从3开始的奇数序列，它是一个无限序列，因为这是一个生成器
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n): #定义一个筛选函数，当x为n的倍数时为False,否则为True
    return lambda x:x % n > 0
def primes():
    yield 2 #2是第一个素数
    it = _odd_iter() # 初始化序列 
    while True:
        n = next(it) #返回序列的第一个数
        yield n 
        it = filter(_not_divisible(n),it) # 构造不是原序列头元素倍数的新序列
for n in primes(): #打印1000内的素数
    if n < 1000:
        print(n)
    else:
        break
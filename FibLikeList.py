class Fib(object):
    def __getitem__(self,n): #用此方法可实现像列表一样按照下标取元素
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f  = Fib()

for n in range(10):
    print(f[n])
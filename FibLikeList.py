class Fib(object):
    def __getitem__(self,n): #用此方法可实现像列表一样按照下标取元素
        if isinstance(n,int):# n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n,slice): #n是切片
            start = n.start
            stop  = n.stop
            if start is None: # 如果切片没有起始值，那么把它设为0，例如：[:5]
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:  #如果当前下标大于切片的开始值，就把对应的元素加到L尾部
                    L.append(a)
                a, b = b, a + b #产生从第0项到第stop-1项fib
            return L


f  = Fib()

for n in range(10):
    print(f[n])

print(f[3:10])
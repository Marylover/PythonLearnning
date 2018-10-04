class Fib(object):

    def __init__(self): #初始化，即Fib的前两项
        self.a, self.b = 0, 1 

    def __iter__(self): #该方法返回一个迭代对象，在此，它返回实例本身
        return self

    def __next__(self):  #获取迭代对象下个值的next方法
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopAsyncIteration()
        return self.a

for n in Fib():
    print(n)
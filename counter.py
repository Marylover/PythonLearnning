def createCounter():
    i = 0
    def counter():
        nonlocal i # 在内部函数给予外部函数局部变量nonlocal声明
        # 让内部函数去其他领域获得这个变量
        i = i + 1
        return i
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

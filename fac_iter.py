def fact_iter(num,product): #尾递归
    if num == 1:
        return product
    return fact_iter(num-1,num*product)
def fact(n):
    return fact_iter(n,1)
print(fact(5))
print(fact(1000))  #python 解释器未对尾递归做优化


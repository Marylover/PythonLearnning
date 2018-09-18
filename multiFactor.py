def multiFactor(a,b,*c):
    s= 1
    s = a*b
    for factors in c :
        s = s*factors 
    return s
a = (1,3,5,7)
b = {2,4,6,8}
print(multiFactor(*a)) ## tuple 可作为参数传入函数做参数
print(multiFactor(*b)) ## dict 可作为参数穿入函数做参数

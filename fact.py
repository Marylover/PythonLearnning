def fac(n):  # 递归法求阶乘
    if n == 1:
        return 1
    return n*fac(n-1)

print(fac(300))

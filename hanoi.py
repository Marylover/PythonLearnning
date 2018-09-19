def hanoi(num,A,B,C): ##递归法实现汉诺塔问题
    if num == 1:
        print(A,'-->',C)
    else :
        hanoi(num-1,A,C,B)
        print(A,'-->',C)
        hanoi(num-1,B,A,C)
hanoi(3,'a','b','c')
import math
def quadratic(a,b,c):
    delt = b**2 -4*a*c
    if delt >=0 :
        x1 = (-b+math.sqrt(delt))/(2*a)
        x2 = (-b-math.sqrt(delt))/(2*a)
        return x1,x2
    else:
        return 'E','R'
x1,x2 = quadratic(2,3,1)
print(x1,x2)
        

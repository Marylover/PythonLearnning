def multiFactor(a,b,*c):
    s= 1
    s = a*b
    for factors in c :
        s = s*factors 
    return s
print(multiFactor(3,5,5,2))
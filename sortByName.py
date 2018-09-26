L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sort_byname(t):
    return t[0]
def sort_byscore(t):
    return t[1]
L2 = sorted(L,key = sort_byname)
L3 = sorted(L,key = sort_byscore)

print(L2,'  by name')
print(L3, '  by score')




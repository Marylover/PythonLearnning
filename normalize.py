def normalize(name):
    Name = {'adam':'Adam','LISA':'Lisa','barT':'Bart'}
    return Name[name]

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
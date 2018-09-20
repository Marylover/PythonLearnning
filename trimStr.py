def trim(s):
    a = 0
    b = 0
    for n in range(len(s)):
        if s[n] == ' ':
            a=a+1
        else :
            break;
    for m in range(len(s)):
        if s[-(m+1)] == ' ':
            b=b+1
        else:
            break 
    return s[a:len(s)-b]
print(trim('  hello  world  ') )
print(len(trim('  hello  world  ')) )
if trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
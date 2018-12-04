print('please input a inter number:')
a = int(input())
result = 0
while a != 0 :
    # result = 0
    carry = a % 10
    a = a // 10
    result = result*10 + carry
print('The result is : ' ,result)



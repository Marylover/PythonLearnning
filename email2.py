import re  #提取电子邮箱中的名字
def name_of_email(addr):
    m = re.match(r'^<?(\w+\s?\w+)>?.*\@[a-zA-Z]+\.\w{3}$', addr)
    return m.group(1)  

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

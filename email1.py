import re  #用正则表达式判断一个字符串是否为合法email地址（简单判断）

def is_valid_email(addr):
    re_email = re.compile(r'^[0-9a-zA-Z\.]+\@[a-zA-Z]+\.com$')
    if re_email.match(addr):
        return True 

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert is_valid_email('a.bill.gates@microsoft.com')
assert is_valid_email('01.bill.gates@microsoft.com')
assert is_valid_email('98bill.gates@microsoft.com')
assert is_valid_email('j9asd.asd9f08.98j.bill.gates@microsoft.com')
assert is_valid_email('1@q.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
assert not is_valid_email('mrbob@.com')
assert not is_valid_email('mrbob@.com.')
assert not is_valid_email('mrbob@com.')
assert not is_valid_email('@a.com')
assert not is_valid_email('x@a.com.')
assert not is_valid_email('@a.com')
print('ok')
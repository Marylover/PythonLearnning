def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2018-9-27')
now()

print(now.__name__)  #注意now()函数__name__属性的变化，为什么变化，我还没想明白
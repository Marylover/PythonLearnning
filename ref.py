import time #from CSDN
import functools
def log_time(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        start=time.time()
        res=func(*args,**kw)
        end=time.time()
        print("%s runned in %s seconds"%(func.__name__,(end-start)*1000))
        return res
    return wrapper

@log_time
def f1(x,y):
    time.sleep(1)
    return x+y

def main():
    result=f1(1,2)
    print(result)

main()

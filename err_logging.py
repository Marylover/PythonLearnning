import logging  #抛出异常，但程序打印完错误信息后继续执行，并正常退出

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()

print('END')  #打印错误信息后执行的代码
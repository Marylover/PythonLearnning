import os
# gitpid(),获得进程名，getppid(),获得父进程名
print('Process (%s) start...'% os.getpid())

pid = os.fork()  
if pid == 0:
    print('I am child process (%s)and my parent is (%s)' %(os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s).'% (os.getpid(),pid))
class Student(object):
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print('My name is %s.'% self.name)

jack = Student('Jack')
print(jack())  #为什么在最后会有一个'None'输出？

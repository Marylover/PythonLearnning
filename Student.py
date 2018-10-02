class Student(object):  #隐藏类中属性，并通过get,set方法访问并改变类的属性
    def __init__(self,name,gender):
        self.__name = name 
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender_new):
        self.__gender = gender_new
        
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')   
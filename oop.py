class Student(object):  #学习python第一个面向对象程序
    def __init__(self,name,score):
        self.name = name
        self.score = score 
    def print_score(self):
        print('%s: %s'%(self.name,self.score))
    def get_grade(self):  #为Student类增加一个方法
        if self.score < 60:
            return 'D'
        elif self.score <= 80:
            return 'C'
        elif self.score <= 85:
            return 'B'
        else:
            return 'A'

mary  = Student('Mary',90)
jack = Student('Jack',70)
mary.print_score()
jack.print_score()
print(mary.name,mary.get_grade())
print(jack.name,jack.get_grade())

class Student(object):  #学习python第一个面向对象程序
    def __init__(self,name,score):
        self.name = name
        self.score = score 
    def print_score(self):
        print('%s: %s'%(self.name,self.score))

mary  = Student('Mary',90)
jack = Student('Jack',95)
mary.print_score()
jack.print_score()
    
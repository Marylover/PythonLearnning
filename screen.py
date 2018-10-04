class Screen(object):  #用@property装饰器把一个方法变成属性调用

    @property   # 有@propetry 和 @ xxx.setter 的为可读可写属性
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value
    
    @property      #只有@propetry的为只读属性
    def resolution(self):
        return self._width*self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
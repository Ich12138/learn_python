# property使用
# 装饰器是在不修改被装饰对象源代码以及调用方式的前提下
# 为被装饰对象添加新功能的可调用对象

# property是一个装饰器,是用来绑定给对象的方法伪造成一个数据属性

# 计算体质参数
class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height * self.height)


obj1 = People('xht', 43, 1.59)
print(obj1.bmi)
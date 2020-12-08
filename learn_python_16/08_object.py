# p366 如何隐藏属性
# 封装是面向对象三大核心特性的一个
# 封装<->整合

# 将封装的属性进行隐藏操作
# 在属性或者方法前面加上 __ 前缀，就会对外实现隐藏属性效果
# 1、在类外部无法直接访问双下滑线开头的属性，但知道了类名和属性名就可以拼出名字：_类名__属性，然后就可以访问了，
# 如Foo._A__N，所以说这种操作并没有严格意义上地限制外部访问，仅仅只是一种语法意义上的变形。

# 2、在类内部是可以直接访问双下滑线开头的属性的，比如self.__f1()，因为在类定义阶段类内部双下滑线开头的属性统一发生了变形。

# 3、变形操作只在类定义阶段发生一次,在类定义之后的赋值操作，不会变形。
# class Foo:
#     __x = 1
#
#     def test1(self):
#         print(self)

# class Foo:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#
# obj = Foo('name', 19)
# print(obj.__dict__)

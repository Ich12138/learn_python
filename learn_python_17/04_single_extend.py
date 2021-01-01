# p374 单继承背景下的属性查找

# 示范一
# class Foo:
#     def f1(self):
#         print('from Foo.f1')
#
#     def f2(self):
#         print('from Foo.f2')
#         self.f1()  # 此时self = obj 所以调用的是obj的f1也就是调用的Bar里的f1
#
#
# class Bar(Foo):
#     def f1(self):
#         print('from Bar.f1')
#
#
# obj = Bar()
# obj.f2()


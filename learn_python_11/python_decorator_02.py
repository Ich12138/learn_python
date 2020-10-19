# 装饰器
"""
1、定义
    器指的是工具,可以定义成函数
    装饰指的是为其他事物添加额外的功能点缀

    合到一起的解释:
        装饰器指的是定义一个函数(或者类), 该函数是用来装饰其他函数的, 即为其他函数增加功能的

2、为何要用装饰器
    开放封闭原则
        开放: 指的是对拓展功能是开放的
        封闭: 指的是对修改源代码是封闭的
    装饰器就是在不修改被装饰器对象源代码以及调用方式的前提下为被装饰的对象添加新功能
"""

# 使用
import time

# 需求 在不修改index函数源代码的情况下以及调用方式的前提下为其添加统计运行时间的功能
# def index(x, y):
#     print("index {}, {}".format(x, y))
#
#
# index(111, 222)
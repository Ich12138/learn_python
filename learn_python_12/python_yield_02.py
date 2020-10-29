"""
三元表达式
    语法格式: 条件成立时要返回的值 if 条件 else 条件不成立返回的值
"""


def func(x, y):
    return x if x > y else y


res = func(3, 4)
print(res)

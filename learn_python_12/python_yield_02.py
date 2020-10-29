"""
三元表达式
    语法格式: 条件成立时要返回的值 if 条件 else 条件不成立返回的值
"""


def func(x, y):
    return x if x > y else y


res = func(3, 4)
print(res)

"""
生成式
    列表生成式
"""
# 提取以s结尾的字符串
l = ['wq_s', 'asd_s', 'asdasd_s', 'zxxc', '456']

# 方式一
# new_l = []
# for s in l:
#     if s.endswith('s'):
#         new_l.append(s)
#
# print(new_l)

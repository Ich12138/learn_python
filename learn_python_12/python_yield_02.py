"""
三元表达式
    语法格式: 条件成立时要返回的值 if 条件 else 条件不成立返回的值
"""

# def func(x, y):
#     return x if x > y else y
#
#
# res = func(3, 4)
# print(res)

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

# 方式二
# new_l = [s for s in l if s.endswith('s')]
# print(new_l)

"""
需求:
    1、把所有小写字母全变成大写
    2、去掉_s后缀
"""

# new_l = [s.upper() for s in l]
# new_l1 = [s.replace('_S', '') for s in new_l]
#
# print(new_l)
# print(new_l1)

# 其他生成式
# 1、字典生成式
# keys = ['name', 'age', 'gender']
# dic = {key: None for key in keys}
# print(dic)


# items = [('name', 'wq'), ('age', 18), ('gender', 'male')]
# dic = {k: v for k, v in items if k != 'gender'}
# print(dic)

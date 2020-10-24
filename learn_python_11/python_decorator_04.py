"""
迭代器
    迭代器指的是: 迭代取值的工具, 迭代是一个重复的过程, 每次重复都是
    基于上一次结果而继续的, 单纯的重复并不是迭代

    迭代器是用来迭代循环取值的工具, 而涉及到多个值循环
    取出来的类型的有: 列表、字符串、元组、字典、集合、文件
    上述迭代取值的方式只适用于有索引的数据类型
    为了解决索引的局限性, python必须提供一种功能不依赖于索引取值的方式, 这就是迭代器

可迭代对象: 但凡内置有__iter__方法的都可称之为可迭代对象
    s = ''
    s.__iter__()

    l = []
    l.__iter__()

    t = (1,)
    t.__iter__()

    d = {"a":1}
    d.__iter__()

    set1 = {1,2,3}
    set1.__iter__()

    with open('./doc/account.txt', mode='w', encoding='utf-8') as f1:
        f1.__iter__()
"""

# 调用可迭代对象下的__iter__()方法会将其转换成迭代器对象
# d = {"a": 1, 'b': 2, 'c': 3}
# d_iterator = d.__iter__()
# print(d_iterator)  # <dict_keyiterator object at 0x02023CF8>

# 简单使用
# print(d_iterator.__next__())
# print(d_iterator.__next__())
# print(d_iterator.__next__())
# print(d_iterator.__next__())  # 抛出异常 StopIteration


# 循环取值
# while True:
#     try:
#         print(d_iterator.__next__())
#     except StopIteration:
#         break

# 可迭代对象与迭代器对象详解
# 可迭代对象("可转成迭代器的对象"): 内置有__iter__()方法的对象
#             可迭代对象.__iter__(): 得到迭代器对象
# 迭代器对象: 内置有__next__()方法并且内置有__iter__方法的对象
#           迭代器对象.__next__(): 得到下一个值
#           迭代器对象.__iter__(): 得到迭代器本身


# d = {"a": 1, 'b': 2, 'c': 3}
# d_iterator = d.__iter__()
# print(d_iterator is d_iterator.__iter__().__iter__())  # True


# for 循环的工作原理: for循环可以称之为迭代器循环
# 1、调用对象的__iter__()得到一个迭代器对象
# 2、调用迭代器对象的__next__()拿到返回值,然后将返回值赋值给k
# 3、循环往复2, 知道抛出StopIteration异常, for循环会捕捉异常然后结束循环

d = {"a": 1, 'b': 2, 'c': 3}
for k in d:
    print(k)


# 可迭代对象: 字符串、列表、元组、字典、集合、文件对象
# 迭代器对象: 文件对象
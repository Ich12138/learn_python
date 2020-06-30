# for循环
# 1、基本使用

'''
语法：
for 变量名 in 可迭代对象: 可迭代对象可以是: 列表，字典，字符串，元组，集合
    代码1
    代码2
    代码3
    ...
'''
# 例一: 列表循环取值
# l = [1, 2, 3, 4, 5]
# for x in l:
#     print(x, end=" ")


# 例二: 字典循环取值
dics = {"k1": 1, "k2": 2, "k3": 3}
for dic in dics:
    print(dic, dics[dic], end="     ")

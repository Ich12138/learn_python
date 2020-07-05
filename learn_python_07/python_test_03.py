# 字典类型
# 定义
# dis = {"k1": 1, "k2": [1, 2, 4], "k3": {"v1": 19}}

# d = {}  # 默认定义出来的是空字典

# d = dict()
# print(d, type(d))
# d = dict(x=1, y=2, z="qwe")
# print(d)


# 数据类型转换
# info = [
#     ["name", "wq"],
#     ("age", 18),
#     ["gender", "male"]
# ]

# d = {}

# 方式一
# for item in info:
#     d[item[0]] = item[1]
# print(d)

# 方式二  利用解压操作
# for k, v in info:
#     d[k] = v
# print(d)


# res = dict(info)
# print(res)


# 创造一个value为None的字典
# 方式一
keys = ["name", "age", "gender"]
# values = None
# d = {}
# for item in keys:
#     d[item] = values
# print(d)


# 方式二
print({}.fromkeys(keys))

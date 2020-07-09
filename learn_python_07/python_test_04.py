# 集合
# 定义：在{}内用逗号分隔开多个元素。，集和具备以下三个特点:
# 1: 每个元素必须是不可变类型
# 2: 集合内没有重复元素
# 3: 集合内元素无序

# 注意1: 列表类型是索引对应值，字典是key对应值，均可以取得单个指定的值，
#       而集合类型既没有索引结构也没有key对应的值，所以无法取得单个值，而且对于
#       集合来说，主要是用于去重，根本没有取出单个值的需求

# 注意2: {}既可以用于定义字典，也可用于定义集合，但是字典里必须是kv键值对，
d = {}  # 默认是空字典
s = set()  # 空集合

# 使用
# s = {1, 2, 3, 4}  # 等价于 s = set({1,2,3,4})
# print(s, type(s))  # {1, 2, 3, 4} <class 'set'>


# 但凡能被for循环的遍历的数据类型（强调：遍历出的每一个值都必须为不可变类型）都可以传给set()转换成集合类型
# s = set([1, 2, 3, 4])

s = set((1, 2, 3, 4))
print(s)

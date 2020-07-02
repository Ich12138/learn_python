# 列表类型
# 定义
# l = [1, 2.3, "a", [1, 2, 3, 4], {"k1": 1}]  # l = list([1, 2.3, "a", [1, 2, 3, 4], {"k1": 1}]) 作用相同
# print(type(l))

# 类型转换：但凡能够被for循环遍历的类型，都可以当作参数传给list()转成列表
# res = list("hello")
# res = list()
res = list({"k1": 1, "k2": 2})
print(res)


# 列表类型
# 定义
# l = [1, 2.3, "a", [1, 2, 3, 4], {"k1": 1}]  # l = list([1, 2.3, "a", [1, 2, 3, 4], {"k1": 1}]) 作用相同
# print(type(l))

# 类型转换：但凡能够被for循环遍历的类型，都可以当作参数传给list()转成列表
# res = list("hello")
# res = list()
# res = list({"k1": 1, "k2": 2})
# print(res)

# 函数
# 1、按照索引取值(正向+反向)：可取可改
l = [1, 2.3, "a", [1, 2, 3, 4], {"k1": 1}]

# 正向取值
# print(l[0])

# 反向取值
# print(l[-1])

# 可存可改
# l[0] = 222
# print(l)

# 2、切片(顾头不顾尾，步长)
# 3、长度
# 4、成员运算 in、not in
# 5、追加 永远在末尾添加
# l.append("asdasdasd")
# print(l)

# 6、插入值
# l.insert(2, "aaaaaaaaa")
# print(l)

# 7、往list里添加list
new_l = ["1", "asd", "4rt"]
# 循环实现
# for item in new_l:
#     l.append(item)
# print(l)

# 函数实现
l.extend(new_l)
print(l)


# 、删除
# 、循环

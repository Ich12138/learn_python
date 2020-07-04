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
# l = [1, 2.3, "a", [1, 2, 3, 4], {"k1": 1}]

# 正向取值
# print(l[0])

# 反向取值
# print(l[-1])

# 可存可改
# l[0] = 222
# print(l)

# 2、切片(顾头不顾尾，步长) 切片就是拷贝行为，相当于浅拷贝
l = [1, 2.3, "a", [1, 2, 3, 4], {"k1": 1}]
# res = l[0:2]
# res = l[0:2]
# print(res)

print(l[::-1])  # 倒置整个列表




# 3、长度
# 4、成员运算 in、not in
# 5、追加 永远在末尾添加
# l.append("asdasdasd")
# print(l)

# 6、插入值
# l.insert(2, "aaaaaaaaa")
# print(l)

# 7、往list里添加list
# new_l = ["1", "asd", "4rt"]
# 循环实现
# for item in new_l:
#     l.append(item)
# print(l)

# 函数实现
# l.extend(new_l)
# print(l)


# 、删除
# l = [1, 2.3, "a", [1, 2, 3, 4], {"k1": 1}]

# 方式1 通用删除方法，没有返回值
# del l[1]
# print(l)

# 方式2 l.pop() 根据索引删除，不指定索引，默认删除最后一个
# item = l.pop()
# item1 = l.pop(2)
# print(item1, l)

# 方式3 l.remove() 根据指定元素删除，没有返回值
# l.remove("a")
# print(l)
# 、循环

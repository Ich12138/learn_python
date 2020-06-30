# 字符串类型的操作
# 定义
# msg = 'hello'
# msg = str('hello')
# 类型转换
# str()函数可以把任意其他类型转化为字符串类型
# dic_str = str({
#     "k1": 2
# })
# print(dic_str)
# 内置方法
# 1、按索引取值(正向取+反向取) 只能取值不能修改
msg = "hello world"

# 正向取
# print(msg[0])

# 反向取
# print(msg[-1])


# 2、切片(顾头不顾尾,步长) 索引的拓展应用
# res = msg[0:5]  # 顾头不顾尾
# print(res)


res = msg[0:5:2]  # 最后一个参数是步长
print(res)

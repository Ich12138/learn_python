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
# msg = "hello world"

# 正向取
# print(msg[0])

# 反向取
# print(msg[-1])


# 2、切片(顾头不顾尾,步长) 索引的拓展应用
# msg = "hello world"
# res = msg[0:5]  # 顾头不顾尾
# print(res)


# res = msg[0:5:2]  # 最后一个参数是步长
# print(res)


# 反向步长
# res = msg[5:0:-1]
# print(res)


# 效果相同
# res = msg[0:11]
# res = msg[:]


# 反转字符串
# res = msg[::-1]
# print(res)


# 3、字符串长度
# msg = "hello world"
# print(len(msg))


# 4、成员运算 in 和 not in
# 判断一个子字符串是否在一个大字符串中
# print("wq" in "wq is nb")
# print("wq" not in "wq is nb")


# 5、移除字符串两端指定符号，但原来的字符串不会改变
msg = "s=+/()       adsasd asdasdasd           =+/()s"
res = msg.strip('s=+/() ')  # 函数默认去掉空格，可以传参数
print(res)

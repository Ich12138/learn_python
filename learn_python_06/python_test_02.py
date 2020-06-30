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
# msg = "s=+/()       adsasd asdasdasd           =+/()s"
# res = msg.strip('s=+/() ')  # 函数默认去掉空格，可以传参数
# print(res)


# 6、切分 split() 把字符串按照某种分隔符进行切分 默认切分空格，返回list
# msg = "hello world asdasda"
# res = msg.split(" ")
# print(res)

# 指定分割次数
# res = msg.split(" ", 1)
# print(res)


# 需要掌握的操作
# 1、strip、lstrip、rstrip
# msg = "***wq***"
# print(msg.strip("*"))  # 去掉两侧的制定字符
# print(msg.lstrip("*"))  # 只去掉左侧指定字符
# print(msg.rstrip("*"))  # 只去掉右侧指定字符

# 2、lower，upper
# msg = "Wwq"
# print(msg.upper())  # 转化为大写
# print(msg.lower())  # 转化为小写


# 3、startswith()、endswith()
# msg = "hello wq world hahaha"
# print(msg.startswith("hello"))  # 是否以特定字符开头
# print(msg.endswith("ha"))  # 是否以特定字符结尾

# 4、split()、rsplit()
# msg = "wq:18:m"
# print(msg.split(":", 1))  # ['wq', '18:m']
# print(msg.rsplit(":", 1))  # ['wq:18', 'm']


# 5、join把列表拼接成字符串
# l1 = ['wq', '18:m']
# res = ":".join(l1)  # 按照某个分隔符，把列表里的全部元素拼接成一个大字符串
# print(res)


# 6、repalce
# msg = "you can you up no can no bb"
# res = msg.replace("you", "YOU", 1)  # 最后一个参数是替换几次，默认全部替换
# print(res)


# 7、isdigit
# 判断字符串是否有纯数字组成
# msg = "123.56"
# print(msg.isdigit())

# 2、条件
# 2.1
# 第一大类：显示布尔值
# 可以直接看出 True False

# 第二大类: 隐式布尔值，所有的值都可以当成条件去用
# 其中0，None,空(空字符串，空列表，空字典)=》代表布尔值为False，其余类型为真


# 3、逻辑运算符
# not:就是把紧跟其后的那个条件结果取反
# ps:not与紧跟其后的那个条件是一个不可分割的整体
# print(not 16 > 13)
# print(not 10)
# print(not 0)
# print(not None)
# print(not "")


# and:逻辑与，用来连接左右两个条件，同真为真，一假则假
print(16 > 1 and True)


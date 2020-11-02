# 面向过程的编程思想
# 核心是"过程"二字,过程及流程,指的是做事的步骤: 先干什么 在干什么 后干什么
# 基于该思想编写程序 就好比在设计流水线
# 优点: 复杂的问题流程化、简单化
# 缺点: 扩展性非常差


# 函数式编程
# 1、有名函数
# func = 函数的内存地址
def func(x, y):
    return x + y


# print(func)  # <function func at 0x0214C028>

# 2、匿名函数: lambda 定义匿名函数
# 编写格式: lambda 参数1,参数2:表达式
# print(lambda x, y: x + y)  # <function <lambda> at 0x014F87C0>

# 3、调用匿名函数: 函数内存地址加()
# 方式一:
# res = (lambda x, y: x + y)(1, 2)
# print(res)

# 方式二:
func1 = lambda x, y: x + y
print(func1)  # <function <lambda> at 0x01DA87C0>
res = func1(2, 3)
print(res)

# 4、匿名函数用于临时调用一次的场景: 更多的是将匿名函数与其他函数配合的场景

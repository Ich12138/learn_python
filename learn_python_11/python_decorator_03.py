"""
有参装饰器
"""

# 一: 知识储备
# 由于语法糖的限制, outer函数只能有一个参数
# 而且该参数只用来接收被装饰对象的内存地址
def outer(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper


@outer
def index(name):
    print("欢迎 {} ".format(name))


index("wq")

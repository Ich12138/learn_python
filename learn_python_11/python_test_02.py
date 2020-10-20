import time


# 1、编写一个函数
# def index(name):
#     print("欢迎 {} 来到主页".format(name))


# 2、编写装饰器, 为函数加上统计时间功能


def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("当前函数 {} 执行时间为: {} s".format(func.__name__, end - start))
        return res

    return wrapper


@time_counter
def index(name):
    time.sleep(2)
    print("欢迎 {} 来到主页".format(name))


index("wq")

# 3、编写装饰器, 为函数加上认证功能
# 4、编写装饰器, 为多个函数加上认证功能, 要求只需登录成功一次, 后续的函数都无需再输入用户名和密码

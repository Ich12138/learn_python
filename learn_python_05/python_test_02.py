# 1、循环的语法与基本使用
"""
while 条件:
      代码1
      代码2
      ....
"""

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# 2、死循环与效率问题
# 纯计算无io的死循环会导致致命的效率问题

# count = 0
# while count < 5:
#     print(count)

# 3、循环的应用

# user_name = "wq"
# user_pwd = "123"
#
# while True:
#     input_name = input("请输入用户名: ")
#     input_pwd = input("请输入密码: ")
#     if input_name == user_name and input_pwd == user_pwd:
#         print("登陆成功")
#         exit()
#         # break
#     else:
#         print("账户或者密码错误!")


# 4、退出循环的两种方式
# (1)修改判断条件
# (2)break关键字


# 7、while循环的嵌套
user_name = "wq"
user_pwd = "123"

while True:
    input_name = input("请输入用户名: ")
    input_pwd = input("请输入密码: ")
    if input_name == user_name and input_pwd == user_pwd:
        print("登陆成功")
        while True:
            cmd = input("请输入指令: ")
            if cmd == "q":
                break
            print("命令{cmd}正在执行".format(cmd=cmd))
        break
    else:
        print("账户或者密码错误!")



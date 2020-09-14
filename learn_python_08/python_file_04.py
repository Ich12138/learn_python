# 文件操作模式详解
# 以t模式为基准进行文件操作
# 1、r(默认操作模式)，只读模式,当文件不存在时,报错,当文件存在时，文件指针跳到最开始位置
# with open('../doc/test.txt', mode='rt', encoding='utf-8') as f:
#     print('第一次读'.center(50, "*"))
#     res = f.read()  # 不加参数，一次性将数据读入内存
#     print(res)
#     print('第二次读'.center(50, "*"))
#     res1 = f.read()
#     print(res1)

# 循环读取文件的每一行
# with open("../doc/test2.txt", mode='rt', encoding='utf-8') as file2:
#     for line in file2:
#         username, password = line.strip().split(':')
#         print('username: {}, passw'
#               'ord: {}'.format(username, password))

# 从文件读取用户名信息验证
# input_username = input('input your username: ')
# input_password = input('input your password: ')
# with open("../doc/test2.txt", mode='rt', encoding='utf-8') as file1:
#     username, password = file1.read().split(":")
# if username == input_username and password == input_password:
#     print("login success")
# else:
#     print('login error')
# 2、wt
# 3、at

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

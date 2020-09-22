# x模式: 只写模式、不可读，不存在则创建，存在就报错

#  文件存在情况下 FileExistsError: [Errno 17] File exists: '../doc/x.txt' 直接报错
# with open('../doc/x.txt', mode='x', encoding='utf-8') as x_file:
#     pass

# 不存在就创建
# with open('../doc/b.txt', mode='x', encoding='utf-8') as x_file:
#     ...

"""
t:
  1、读写都是以字符串形式的
  2、只能针对文本文件
  3、必须指定字符编码
b:binary模式
  1、读写都是以bytes为单位
  2、可以针对所有文件
  3、一定不能指定encoding参数
"""
# 读模式
with open(r'../doc/x.txt', mode='rb') as f1:
    res = f1.read()  # utf-8的二进制
    print(res)
    print(type(res))  # bytes类型  <class 'bytes'>
    print(res.decode('utf-8'))

# 写模式
with open(r'../doc/test1.txt', mode='wb') as f2:
    f2.write('王骞'.encode('utf-8'))

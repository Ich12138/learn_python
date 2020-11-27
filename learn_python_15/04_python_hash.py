# p356 hash介绍
"""
hash
    hash是一类算法, 该算法接受传入的内容, 经过运算的到一串hash值
特点:
    1、只要传给的内容一样, 则结果就一定一样
    2、不能由hash值反解回内容
    3、只要使用的hash算法不变, 无论传入的内容有多大, 得到的hash长度不变

用途:
    1、密码加密
    2、文件完整性校验
"""

# p357 hashlib使用
import hashlib

m = hashlib.md5()
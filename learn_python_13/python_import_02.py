# 循环导入问题

# 模块搜索优先级
# from foo import x
# import foo
# 无论是import ... 还是 from ... import ...再导入模块时都涉及到优先级问题
# 优先级:
# 1、内存(内置模块)
# 2、从硬盘找 按照sys.path 中存放的文件顺序依次查找要导入的模块

import sys

# 值为第一个列表, 存放了一系列文件夹
# 其中第一个文件夹是当前执行文件所在的文件夹
print(sys.path)

# sys.modules查看已经加载到内存中的模块
print(sys.modules)

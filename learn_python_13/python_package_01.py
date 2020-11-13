# python包的使用
"""
1、包就是一个包含有__init__.py的文件夹 见python_package_test文件夹

2、包的作用
    包的本质是模块的一种形式
    包是用来被当作模块导入
"""
# 1、产生一个名称空间
# 2、运行包下的__init__.py文件, 将运行过程中产生的名字都丢到1的名称空间中
# 3、在当前执行文件的名称空间中拿到一个名字python_package_test,该名字是指向1的名称空间
import python_package_test
print(python_package_test.x)
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

count = 0
while count < 5:
    print(count)

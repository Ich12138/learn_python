# p342 sys模块
# import sys
#
# # 获取的是解释器后参数值
# print(sys.argv)

# p343 打印进度条
import time

# res = ''
# for i in range(100):
#     res += '#'
#     time.sleep(0.5)
#     print('\r[%-50s]' % res, end='')

# 模拟文件下载, 打印进度条
recv_size = 0
total_size = 3333333
while recv_size < total_size:
    time.sleep(0.001)
    recv_size += 1024

    percent = recv_size / total_size
    res = int(50 * percent) * '#'
    print('\r[%-50s] %d%%' % (res, int(percent * 100)), end='')

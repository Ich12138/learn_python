# 通用公共库函数
import time


# 记录日志功能
def logger(msg):
    with open(r'F:\Jetbrains\PythonSoftWare\PythonProjects\learn_python\learn_python_13\ATM\log\user.log', mode='at',
              encoding='utf-8') as log_f:
        log_f.write('%s %s\n' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg))
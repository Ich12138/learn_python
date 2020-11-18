# p334 时间模块1
import time
# 一: time
# 时间分为三种格式:

# 1、时间戳: 从1970年到现在经历过的描述
# 应用: 用于时间间隔的计算
# print(time.time())  # 1605687690.4247599

# 2、格式化的字串的时间格式:
# 应用: 用于展示
# print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 2020-11-18 16:21:30
# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))  # 2020-11-18 16:21:30 PM
# print(time.strftime('%Y-%m-%d %X'))  # 2020-11-18 16:21:30

# 3、结构化时间
# 应用: 用于单独获取时间的某一部分
# res = time.localtime()
# print(res)  # time.struct_time(tm_year=2020, tm_mon=11, tm_mday=18, tm_hour=16, tm_min=23, tm_sec=11, tm_wday=2, tm_yday=323, tm_isdst=0)
# print('当前的年份: {}'.format(res.tm_year))
# print('今天是今年的第几天: {}'.format(res.tm_yday))


# p335 时间模块2
# 二: datetime
import datetime
# print(datetime.datetime.now())  # 2020-11-18 16:31:09.666523
# print(datetime.datetime.now() + datetime.timedelta(days=-3))
# print(datetime.datetime.now() + datetime.timedelta(weeks=-3))

# p336 时间模块3
# 时间模块需要掌握的操作
# 一: 时间格式的转换

# 结构化时间 -> 时间戳
# s_time = time.localtime()
# print(time.mktime(s_time))

# 时间戳 -> 结构化时间
# tp_time = time.time()
# print(time.localtime(tp_time))

# print(time.localtime())  # 本地时间    time.struct_time(tm_year=2020, tm_mon=11, tm_mday=18, tm_hour=16, tm_min=53, tm_sec=31, tm_wday=2, tm_yday=323, tm_isdst=0)
# print(time.gmtime())  # 世界标准时间  time.struct_time(tm_year=2020, tm_mon=11, tm_mday=18, tm_hour=8, tm_min=53, tm_sec=20, tm_wday=2, tm_yday=323, tm_isdst=0)

# print(time.localtime(tp_time))
# print(time.gmtime(tp_time))

# 结构化时间 -> 格式化时间
# s_time = time.localtime()
# res = time.strftime('%Y-%m-%d %H:%M:%S', s_time)
# print(res)

# 格式化时间 -> 结构化时间
# format_time = '2035-11-11 16:56:54'
# res = time.strptime(format_time, '%Y-%m-%d %H:%M:%S')
# print(res)
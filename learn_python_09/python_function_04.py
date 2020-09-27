# 作业
# 1、写函数，统计传入的字符串中 数字、字母、空格、以及 其他的个数
def str_count(my_str):
    dis = {
        'number': 0,
        'letter': 0,
        'blank': 0,
        'other': 0,
    }
    for item in my_str:
        if item.isspace():
            dis['blank'] = dis['blank'] + 1
        elif item.isalpha():
            dis['letter'] = dis['letter'] + 1
        elif item.isdigit():
            dis['number'] = dis['number'] + 1
        else:
            dis['other'] = dis['other'] + 1
    print(dis)


str_count('1q* ')

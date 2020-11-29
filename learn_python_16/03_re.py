# p368 正则表达式
import re

# 匹配字母下划线
# res = re.findall('\w', 'abc123_*()-=')
# print(res)

# 匹配非字母下划线
# res = re.findall('\W', 'abc123_*()-= ')
# print(res)

# 匹配任意空白字符 [\t\r\n\f]
# res = re.findall('\s', 'ab\fc123\n_*()\t-=')
# print(res)

# 匹配非空字符 [\t\r\n\f]
# res = re.findall('\S', 'ab\fc123\n_*()\t-=')
# print(res)

# 匹配任意数字 [0-9]
# res = re.findall('\d', 'ab\fc123\n_*()\t-=')
# print(res)

# 匹配非数字字符
# res = re.findall('\D', 'ab\fc123\n_*()\t-=')
# print(res)

# 匹配字符串开始 只匹配开头
# res = re.findall('\Axxx', ' xxxab\fcxxx123\n_*()\t-=')
# print(res)

# 匹配字符串结束, 如果存在换行, 只匹配到换行前结束的字符
# res = re.findall('xxx\Z', ' xxxab\fcxxx123\n_*()\t-=xxx')
# print(res)

# 匹配字符串开头
# res = re.findall('^xxx', 'xxxab\fcxxx123\n_*()\t-=xxx')
# print(res)

# 匹配字符串的末尾
res = re.findall('xxx$', 'xxxab\fcxxx123\n_*()\t-=xxx')
print(res)
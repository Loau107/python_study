import re

try:
    # 参数 1 : 正则表达式　参数 ２ : 字符串数据
    ret = re.match('\w\w\s\w\w\w', 'ni hao')
    # 获取提取的数据
    info = ret.group()
except Exception as e:
    print(e)
else:
    print(info)


# 匹配单个字符
# .　任意一个字符
# [] 列表中的字符
# \d 数字字符 0-9   \D 非数字字符
# \s 空格/tab字符   \S 非空格
# \w 非特殊字符 a-z A-Z 0-9 _ 汉字   \W 非特殊字符

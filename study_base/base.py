# 输入输出函数
# print('hello world!')
# print('hello', end = ' ') # end 为结尾符， 默认为 '\n'
# print('world!')
# print('hello', 'world', sep = '&') # sep 为分隔符， 默认为空格 ' '
# str = input('请输入一个字符串：') # 返回字符串类型
# num = int(input('请输入一个数字：')) # 字符串类型转换为整形

# 函数定义
# def getSum(a, b):
#     return a + b
# def getSum1(a, b = 5): # 可以真参数设置一个默认值，当调用函数时不传入此参数，会使用这个默认值
#     return a + b
# print(getSum1(3))
# a = getSum(3, 5)
# print(a)
# def max(a, b):
#     return a if a > b else b # python中的三元运算符
# print(max(1, 5))


# 类
# class Student:
#     def __init__(self, name, age, score): # 构造函数，默认格式
#         self.name = name
#         self.age = age
#         self.score = score
#     def get_score(self): # self 表示调用的对象本身
#         print(self.name + "同学，您的期末总分数为：" + str(self.score))
# stu = Student('雷国丽', 18, 0)
# stu.get_score()
# print('祝你挂科愉快！！！')


# 数字处理函数
# print(abs(-3)) #绝对值
# print(round(2.5)) #四舍六入五凑偶
# print(pow(2, 3)) #幂
# import math
# print(math.cell(3.5)) #把小数补全:4


# 字符串处理函数
# string = 'hello wolrd!'
# print(string[0:5]) #返回[0, 5)这个索引区间的字符片段
# print(len(string)) # 获取字符串长度
# string = string.replace('wolrd', 'world') #后面字符片段替换前面字符片段
# print(string)
# print(string.find('lo')) #返回字符片段索引
# print(string.split(' ', 1)) #切割字符串，第二个参数为切割的次数，默认是无上限的，可以省略


# 列表
# list = [3, 4, 2, 5, 1] #列表中的元素类型可以混搭，但一般会使用统一类型
# print(list[2])
# list.append(6) # 添加元素
# print(list)
# list.pop(5) # 删除指定索引元素，参数为索引，默认为最后一项，可以省略
# print(list)
# list.insert(2, 6) # 插入元素，参数1为索引，参数2为元素
# print(list)
# list.remove(6) # 删除指定元素，参数为元素值
# print(list)
# list.sort() # 按自然顺序排列
# print(list)
# list.reverse() # 反序排列
# print(list)
# print(list.index(5)) # 获取元素 的索引


# 元组
# 元组与列表相似，只是元素和元素的长度都是不可变的，是完全固定的
# tup = (1, 2, 3) # 全称 tuple
# print(len(tup))
# print(tup[0:3])
# L = list(tup) # 元组转换为列表
# L.append(4)
# print(L)
# T = tuple(L) # 列表转换为f元组
# print(T)


# 字典
# 字典可以理解为双列的列表，是一种键值对的形式
# dict = { # 全称 dictionary
#     'name' : "au", # 左边是键，右边是值，键只能用字符串类型，值可以为任意类型
#     'age' : 18,
#     'score' : 100
# }
# print(dict['name']) # 通过键查找值
# print(len(dict)) # 获取键值对个数
# print(dict.keys()) # 获取所有的键，返回一个列表格式的字符串
# print(dict.values()) # 获取所有的值，返回一个列表格式的字符串
# dict['sex'] = '男' # 添加一个键殖对
# print(dict)
# dict.pop('name') # 删除一个键值对
# print(dict)


# 集合
# 集合相当于一个无序（无下标）无重（无重复元素）的列表
# set1 = {2, 4, 5, 3, 1, 2, 3, 4, 5}
# print(set1) # 输出的时候会按值的自然顺序输出，但是集合本来是没有排序的
# set2 = {3, 4, 5, 6, 7}
# print(set1.intersection(set2)) # 求两个集合的交集
# print(set1.difference(set2)) # 两个集合的交集在前集合中的补集
# set3 = {1, 2, 3}
# print(set3.issubset(set1)) # 判断前者是否为后者的子集
# print(set3.issubset(set2))


# 值类型与引用类型
# a = 1
# b = a
# b = 3 # 值类型的操作
# print(a)
# list1 = [1, 2, 3]
# list2 = list1
# list2[1] = 5 # 引用类型的操作
# print(list1)
# list2 = [2, 3, 4] # 值类型的操作
# print(list1)


# 条件控制
# hemowork_finished = True
# if hemowork_finished:
#     print('可以去玩了')
# else:
#     print('滚回去写作业')
# num = int(input("请输入一个整数："))
# if num >= 0 and num < 10: # and <=> &&，or <=> ||，not() <=> !()
#     print(str(num) + '是一位数')
# elif num >= 10 and num < 100: # elif <=> else if
#     print(str(num) + '是两位数')
# else:
#     print(str(num) + '是三位或三位以上的数')

# 补充：Python里面没有switch这个控制语句，一般用 if-elif-else 来替代


# 序列
# range(开头，结尾，间距)
# 传入一个参数时为结尾，而开头默认为 0
# 传入两个参数时为开头与结尾
# print(list(range(10)))
# print(list(range(10, 20)))
# print(list(range(0, 20, 3)))


# 循环
# while 循环
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# # for 循环
# for i in range(10):
#     print(i)
# list = [13, 14, 24, 25, 36]
# for num in list:
#     print(num)
# for i in range(len(list)):
#     print(list[i])

# 枚举
# a = ['hello', 'world', 'python']
# b = enumerate(a) # enumerate() 函数，返回一个枚举类的对象
# print(b)
# l = list(b)
# print(list(b)[1])
# 加行号
# with open('file/test.txt') as fr:
#     enum = list(enumerate(fr))
# with open('file/test.txt', 'w') as fw:
#     for i, key in enum:
#         fw.write(f'{i} {key}')
# 加行号升级版
# with open('file/test.txt', 'r+') as f:
#     lines = f.readlines() # 返回元素为每行的列表，带'\n'的
#     lines = [str(key + 1) + ' ' + value for key, value in enumerate(lines)]
#     f.seek(0)
#     f.truncate() # 清空原数据
#     for line in lines: # 重新写入数据
#         f.write(line)
# 文件操作
# 模式：1、r只读，2、w写入并替换，3、x只创建写入，4、a追加模式，5、b二进制模式，6、t文本模式，7、r+读写模式
# f1 = open('src\\study\\IO流\\test.txt') #默认 r 只读模式
# print(f1.read())
# f1.close()
# f2 = open('src\\study\\IO流\\test.txt', 'w') #打开一个 w 写入模式
# f2.write('hello\nworld')
# f2.close()

# f = open('file/IO/test.txt', 'w')
# f.write('hello world, welcome to Luffycity3.\n')
# f.write('hello world, welcome to Luffycity3.\n')
# f.write('hello world, welcome to Luffycity3.\n')
# f.seek(10) # 将光标移动到第 10 个字节的位置
# print(f'在第 {f.tell()} 个位置添加 "ten"') # tell() 返回当前光标位置
# f.write('"ten"')
# f.seek()
# f.truncate() # 清空当前光标下面的内容
# f.flush # 将缓冲区的内容刷新到文件中
# f.close()

# f = open('file/IO/student.txt', 'r+')
# str = f.read()
# str_new = str.replace('吴浩', '梁鹏潘') # 用后面的内容替换前面的内容
# print(str_new)
# f.seek(0)
# f.truncate() # 清空原文件
# f.write(str_new) # 重新写入
# f.close()
# import os
# os.remove('file/IO/password.txt') # 删除文件

# fr = open('file/IO/mac_5K.jpg', 'rb')
# str = fr.read()
# fr.close()
# fw = open('file/IO/copy.jpg', 'wb')
# fw.write(str)
# fw.close()

# f = open('file/IO/test.py', 'wb')
# str = "print('这是一个二进制文件\\n')\n".encode('utf-8') # encode() 编码：把 Unicode（统一码） 编码为字符串的字节类型
# f.write(str)
# f.close()
# print(str.decode('utf-8')) # decode() 解码：把字符串的字节类型解码为 Unicode（统一码）

# 序列化与反序列化
# import pickle
# with open('file/exception/test.txt', 'wb') as f:
#     a1 = '字符串'
#     a2 = 234
#     a3 = [20, 30, 40]
#     # 序列化 语法: pickle.dump(obj, file)，obj 为任意对象，file 为路径
#     pickle.dump(a1, f)
#     pickle.dump(a2, f)
#     pickle.dump(a3, f)
# with open('file/exception/test.txt', 'rb') as f:
#     # 反序列化 语法: pickle.load(file), file 为路径
#     a1 = pickle.load(f) # 按行读取
#     a2 = pickle.load(f)
#     a3 = pickle.load(f)
#     print(a1)
#     print(a2)
#     print(a3)

# CSV 文件的操作
# CSV 是逗号分隔文本格式，常用于数据交换，Excel 文件和数据库文件的导入导出，与 Excel 文件不同，CSV 文件中：
# 1、值没有类型，所有值都是字符串 2、不能指定字体颜色等样式 3、不能指定单元宽高，不能合并单元格 4、没有多个工作表 不能嵌入图像图表
# import csv
# with open('file/exception/test.csv') as f:
#     r_csv = csv.reader(f)
#     for row in r_csv:
#         print(row)
# with open('file/exception/test.csv', 'w') as f:
#     w_csv = csv.writer(f) # 获得写入器
#     w_csv.writerow(['姓名', '年龄', '分数'])
#     w_csv.writerow(['吴浩', '18', '99'])
#     w_csv.writerow(['wuhao', '18', '99'])
#     lists = [['au', '19', '88'], ['loau', '19', '89']]
#     w_csv.writerows(lists)

import os

# 获取系统相关信息
# print(os.name) # 获取操作系统名称   windows : nt   linux / unix : posix
# print(os.sep) # 路径分隔符   windows ： \   linux / unix : /
# print(repr(os.linesep)) # 换行符   windows : '\r\n'    linux / unix : '\n'

# 获取文件与文件夹的信息
# print(os.stat('study/OS/os.py')) # stat() 返回文件或目录的属性
# print(os.stat('study/OS'))

# 关于工作目录的操作
# print(os.getcwd()) # 获取当前的工作目录
# os.chdir('/home/loau/python/project/study/OS') # 更改当前工作目录
# os.mkdir('书籍') # 创建目录
# os.rmdir('书籍') # 删除目录
# os.makedirs('a/b/c') # 创建多级目录
# os.removedirs('a/b/c') # 删除多级目录
# os.rename('os.py', 'OS.py') # 重命名目录
# dirs = os.listdir('../../') # 获取当前目录下的子文件和子目录
# print(dirs)

# os.path 模块
# 判断
# isabs(path) # 判断 path 是否绝对路径
# isdir(path) # 判断 path 是否为目录
# isfile(path) # 判断 path 是否为文件
# exists(path) # 判断指定路径的文件是否存在
# 返回文件信息
# getsize(filename) # 返回文件的大小
# abspath(path) # 返回绝对路径
# dirname(path) # 返回目录的路径
# 返回时间
# getatime(filename) # 返回文件的最后访问时间
# getmtime(filename) # 返回文件的最后修改时间
# 遍历
# walk(top, func, arg) # 遍历方式遍历目录
# 路径拼接与切割操作
# join(path, *paths) # 连接多个path
# split(path) # 对路径进行分割，以列表形式返回
# splitext(path) # 从路径中分割文件的扩展名

# walk() 递归遍历所有子目录和子文件
# path = os.getcwd()
# list_files = os.walk(path)
# all_files = [] # 存储所有子目录及子文件
# for dirpath, dirnames, filenames in list_files:
#     for dir in dirnames: # 遍历所有子目录
#         print(dir)
#         all_files.append(os.path.join(dirpath, dir))
#     for file in filenames: # 遍历所有子文件
#         print(file)
#         all_files.append(os.path.join(dirpath, file))
# for file in all_files: # 遍历所有子目录和子文件
#     print(file)


# shutil 模块
import shutil

# 文件与目录的拷贝
# shutil.copyfile('file/OS/test.txt', 'file/OS/copytest.txt') # 拷贝文件
# shutil.copytree('file/OS', 'file/OS/copyOS') # 拷贝目录及目录下文件
# shutil.copytree('file/OS', 'file/OS/copyOS', ignore=shutil.ignore_patterns('*.py', '*.html')) # 拷贝目录及文件，带有 ignore 中后缀的文件不拷贝

# 压缩与解压缩
# shutil.make_archive('file/OS/test', 'zip', 'file/OS/test') # 目标路径及压缩后名字，压缩包后缀，压缩原目录

import zipfile
# zipfile 模块压缩
# z = zipfile.ZipFile('file/OS/test.zip', 'w') # 获取压缩器
# z.write('file/OS/test/test1.txt') # 把整个路径都压缩进压缩包，但不会把子目录及子文件压缩进去
# z.write('file/OS/test/test2.txt')
# z.close()
# zipfile 模块解压缩
# z = zipfile.ZipFile('file/OS/test.zip', 'r') # 获取解压缩器
# z.extractall('file/OS/test') # 解压缩到指定目录
# z.close()
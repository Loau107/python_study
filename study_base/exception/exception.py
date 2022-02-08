# try:
#     print(3 / 0)
# except BaseException as e: # ZeroDivisionError
#     print('发生异常， 0 不能做除数')
#     print(e)
#     print(type(e))

# while True:
#     try:
#         x = int(input('请输入一个数字：'))
#         print(f'输入的数字为：{x}')
#         if x == 0:
#             print('退出程序！')
#     except: # ValueError
#         print('发生异常，输入的不是数字！')

# # try...except...
# while True:
#     try:
#         x = int(input('请输入被除数：'))
#         y = int(input('请输入除数：'))
#         print(f'{x} / {y} = {x / y}')
#     except ZeroDivisionError:
#         print('发生异常，除数不能为零！')
#     except ValueError:
#         print('发生异常，输入的不是数字！')
#     except BaseException as e:
#         print(e)

# # try...except...else...
# while True:
#     try:
#         x = int(input('请输入被除数：'))
#         y = int(input('请输入除数：'))
#         m = x / y
#     except BaseException:
#         print('发生异常！')
#     else:
#         print(f'{x} / {y} = {m}')

# # try...except...else...finally...
# while True:
#     op = input('是否编码(Y/N)：')
#     if op == 'Y' or op == 'y':
#         str = 'hello world!\n'.encode('utf-8')
#     elif op == 'N' or op == 'n':
#         str = 'hello world!\n'
#     elif op == '0':
#         print('退出程序！')
#         exit()
#     else:
#         print('输入错误！')
#     try:
#         f = open('file/exception/test.txt', 'ab') #二进制追加模式
#         f.write(str)
#     except BaseException as e:
#         print('发生异常，写入失败！')
#         print(f'异常类型为：{e}')
#     else:
#         print(f'已写入数据：{str}')
#         print('写入完毕！')
#     finally:
#         f.close()

# # with 自动释放资源
# with open('file/exception/test.txt') as f:
#     str = ''.join(f.read())

# # traceback 模块
# import traceback
# try:
#     num = 3 / 0
#     print(num)
# except:
#     traceback.print_exc()
# ##### 将异常信息输出到文件中 #####
# try:
#     print(3 / 0)
# except:
#     with open('file/exception/tracebaek_test.txt', 'a') as f:
#         traceback.print_exc(file = f)

# # 自定义异常
# class AgeError(Exception): # 年龄异常
#     def __init__ (self, errorInfo):
#         Exception.__init__(self) # 调用父类构造方法
#         self.errorInfo = errorInfo
#     def __str__(self):
#         return f'年龄: {self.errorInfo} 错误，应该在 1 - 150 之间！'
# ##### 测试代码 #####
# if __name__ == '__main__': # 如果程序为直接调用，则内置变量__name__的值为__main__，否则为调用脚本本身的名字
#     new_age = int(input('请输入您的年龄：'))
#     if new_age < 1 or new_age > 150:
#         raise AgeError(new_age) # 抛出异常
#     else:
#         print(f'您的年龄为{new_age}')

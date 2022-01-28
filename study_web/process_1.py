# import multiprocessing
# import time
#
# g_num = []
#
# def write():
#     '''向全局变量 g_num 写入数据'''
#     global g_num
#     for i in range(5):
#         g_num.append(i)
#     print('my_write :', g_num)
#
# def read():
#     '''读取全局变量 g_num 的值'''
#     global g_num
#     print('my_read :', g_num)
#
# if __name__ == '__main__':
#     my_write = multiprocessing.Process(target=write)
#     my_read = multiprocessing.Process(target=read)
#     my_write.start()
#     time.sleep(1) # 保证数据能正常写入 g_num 中
#     my_read.start()

# 输出结果：
# my_write : [0, 1, 2, 3, 4]
# my_read : []

# 结论：
# 进程之间不共享全局变量



# 守护进程
# import multiprocessing
# import time
#
# def func():
#     for i in range(5):
#         time.sleep(0.2)
#         print('子进程')

# if __name__ == '__main__':
#     # 程序一旦运行 就会默认创建主进程
#     my_func = multiprocessing.Process(target=func) # 主进程创建子进程
#     my_func.start() # 主进程开启子进程
#     for i in range(3):
#         time.sleep(0.2)
#         print('主进程')
#     print('主进程 : over')

# 运行结果：
# 主进程 : over
# func
# func
# func
# func
# func

# 结论：
# 主进程和子进程会同时进行
# 但是默认情况下 主进程会等待子进程结束之后再结束

# 解决方法：
# 1、可以把子进程设置为守护进程 守护进程会随着主进程的结束一起结束
# 2、在主进程结束时手动销毁子进程

# if __name__ == '__main__':
#     # 方法一：设置守护进程
#     my_func = multiprocessing.Process(target=func, daemon=True) # 一、可以在创建进程时就设置 daemon 为 True
#     # my_func.daemon = True # 二、也可以在创建之后，再设置 daemon 为 True
#     my_func.start()
#     for i in range(3):
#         time.sleep(0.2)
#         print('主进程')
#     # 方法二：手动结束子进程
#     # my_func.terminate()
#     print('主进程 : over')
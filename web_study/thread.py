# 多线程使用
# 1、导入模块 threading
# 2、创建子线程 threading.Thread()
# 3、启动子线程 start()

# import threading
# import time
#
# def dance(count):
#     for i in range(count):
#         time.sleep(1)
#         print('跳舞', i)
#
# def sing(count):
#     for i in range(count):
#         time.sleep(1)
#         print('唱歌', i)
#
# if __name__ == '__main__':
#     my_dance = threading.Thread(target=dance, args=(5,))
#     my_sing = threading.Thread(target=sing, kwargs={'count':5})
#     my_dance.start()
#     my_sing.start()


# 守护线程
# import threading
# import time
#
# def func():
#     for i in range(5):
#         time.sleep(0.2)
#         print('func')
#
# if __name__ == '__main__':
#     my_func = threading.Thread(target=func, daemon=True) # 方法一：创建线程时直接设置 daemon 为 True
#     my_func.start()
#     time.sleep(0.5)
#     # my_func.setDaemon(True) # 方法二：使用 setDeamon() 函数设置
#     print('over')


# 注意点：
# 1、线程之间是无序执行的（进程之间也是无序执行的）
# 2、线程之间共享全局变量


# 线程之间共享全局变量
# import threading
# import time
#
# g_num = []
#
# def write():
#     global g_num
#     for i in range(5):
#         g_num.append(i)
#     print('write :',g_num)
#
# def read():
#     global g_num
#     print('read :', g_num)
#
# if __name__ == '__main__':
#     my_write = threading.Thread(target=write)
#     my_read = threading.Thread(target=read)
#     my_write.start()
#     time.sleep(1)
#     my_read.start()


# 线程之间共享全局变量问题
# import threading
# import time
#
# g_num = 0
#
# def sum_num1():
#     global g_num
#     for i in range(1000):
#         time.sleep(0.0001)
#         g_num += 1
#     print('sum_num1 :', g_num)
#
# def sum_num2():
#     global g_num
#     for i in range(1000):
#         time.sleep(0.0001)
#         g_num += 1
#     print('sum_num2 :', g_num)

# if __name__ == '__main__':
#     sub_num1 = threading.Thread(target=sum_num1)
#     sub_num2 = threading.Thread(target=sum_num2)
#     sub_num1.start()
#     sub_num2.start()
#     time.sleep(2.5)
#     print('g_num :', g_num)

# 执行结果示例：
# sum_num1 : 126247
# sum_num2 : 127294
# 分析：
# 假设刚开始 g_num == 0
# 在线程一获取 g_num == 0 后到抢占 CPU 进行 g_num++ 操作结束前的过程中，可能会被线程二抢走 CPU 使用权
# 而线程二获取的 g_num 的值也为 0，这时线程二进行 g_num++ 并返回 1 到 g_num 中
# 接着线程一又抢回 CPU 使用权并继续进行 g_num++ 操作，此时得到的 g_num 结果也为 1
# 则线程一、线程二进行了分别进行的一次自加操作，合起来只增加了 1

# 解决方法：
# 方法一：让线程二等待线程一结束后再运行线程二，此方法相当于两个线程合成了一个线程，不实用
# 方法二：使用互斥锁 步骤：1、创建锁 2、设置锁 3、释放锁（否则会）
# 互斥锁：相当于给一个资源上了一个锁，每次只能提供给一个线程使用，保证了同一时刻只能有一个线程进行操作
import threading
import time

g_num = 0

mutex = threading.Lock() # 创建锁

def sum_num1():
    global g_num
    for i in range(1000):
        time.sleep(0.0001)
        mutex.acquire() # 设置锁
        g_num += 1
        mutex.release() # 释放锁
    print('sum_num1 :', g_num)

def sum_num2():
    global g_num
    for i in range(1000):
        time.sleep(0.0001)
        mutex.acquire() # 设置锁
        g_num += 1
        mutex.release() # 释放锁
    print('sum_num2 :', g_num)

if __name__ == '__main__':
    sub_num1 = threading.Thread(target=sum_num1)
    sub_num2 = threading.Thread(target=sum_num2)
    sub_num1.start()
    # sub_num1.join() # 方法一：设置进程等待
    sub_num2.start()
    time.sleep(1.1)
    print('g_num :', g_num)
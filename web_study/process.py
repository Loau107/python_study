# 多任务
# 并发
# 在一段时间内交替去执行多个任务（只有一个 CPU）
# 并行
# 在同一时刻执行多个任务（多核 CPU）

# 进程（多任务的实现方式）
# 进程: 一个正在运行的程序就是一个进程, 它是操作系统进行资源分配的基本单位（最小单位）

# 线程
# 线程：使用资源的最小单位

# 测试代码
import time
import os

def dance(count):
    for i in range(count):
        time.sleep(1)
        print('跳舞', i)
        # print('dance id :', os.getpid()) # 获取进程 ID
        # print('father id :', os.getppid())
        # print(multiprocessing.current_process()) # 获取进程名
def sing(count):
    for i in range(count):
        time.sleep(1)
        print('唱歌', i)
        # print('sing id :', os.getpid())
        # print('father id :', os.getppid())
        # print(multiprocessing.current_process())

# 单进程
# 需要 10 秒钟完成
# 最少有一个进程 这个进程中最少有一个线程
# if __name__ == '__main__':
#     test.dance(5)
#     test.sing(5)


# 多进程
# 需要 5 秒钟完成（提升执行效率）
# 注意！！！
# 这里其实有 3 个进程，1 个主进程，2 个子进程
# 3 个线程：每个进程里有一个线程
import multiprocessing # 导入进程模块
if __name__ == '__main__':
    # 创建子进程
    # target : 指定执行的任务（函数）
    # name : 给子进程设置名字
    # args : 用元组的格式传入任务（函数）的参数（注意：单个元素的元组要加上','）
    # kwargs : 用字典的格式传入任务（函数）的参数（注意：key 应为参数名，对应的 value 应为参数的值）
    my_dance = multiprocessing.Process(target=test.dance, name='dance', args=(5,))
    # my_sing = multiprocessing.Process(target=test.sing, name='sing', args=(5,))
    my_sing = multiprocessing.Process(target=test.sing, name='sing', kwargs={'count': 5})
    # 开启子进程
    my_dance.start()
    my_sing.start()
import multiprocessing
import time

g_num = []

def write():
    '''向全局变量 g_num 写入数据'''
    global g_num
    for i in range(5):
        g_num.append(i)
    print('my_write :', g_num)

def read():
    '''读取全局变量 g_num 的值'''
    global g_num
    print('my_read :', g_num)

if __name__ == '__main__':
    my_write = multiprocessing.Process(target=write)
    my_read = multiprocessing.Process(target=read)
    my_write.start()
    time.sleep(1) # 保证数据能正常写入 g_num 中
    my_read.start()
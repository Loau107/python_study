# 装饰器：在不修改原有的函数代码的前提下 给函数增加新的功能
# def func_out(func):
#     def func_in():
#         print('验证')
#         func()
#     return func_in
#
# @func_out # login = func_out(login)
# def login():
#     print('登录')
#
# login()



# 案例：计算函数执行时间
# import time
#
# # 给函数增加计算时间的功能
# def time_demo(func):
#     def func_inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print('使用时间：%.2f' % (end_time - start_time))
#
#     return func_inner
#
# @time_demo
# def test():
#     for i in range(100000):
#         print(i)
#
# if __name__ == '__main__':
#     test()



# 通用格式的装饰器
# def func_out(func):
#     def func_in(*args, **kwargs):
#         ret = func(*args, **kwargs)
#         return ret

#     return func_in

# @func_out
# def my_test(*args, **kwargs):
#     for i in args:
#         print(i)
#     for key, value in kwargs.items():
#         print(key, '=', value)

# my_test(10, 20, 30, new_age = 18, name = 'au', score = 100)



# 多层装饰器
# def func_out_1(func_1):
#     print('this is func_out_1')
#     def func_in_1():
#         print('this is func_in_1')
#         func_1()
#
#     return func_in_1
#
# def func_out_2(func_2):
#     print('this is func_out_2')
#     def func_in_2():
#         print('this is func_in_2')
#         func_2()
#
#     return func_in_2
#
# @func_out_2 # login = func_out_2(login)
# @func_out_1 # login = func_out_1(login)
# def login():
#     print('this is login')
#
# login()
'''
@func_out_1
    print('this is func_out_1')
第一层包装后 login():
    login() == func_in_1():
        print('this is func_in_1')
        print('this is login')
'''
'''
@func_out_2
    print('this is func_out_2')
第二层包装后 login():
    login() == func_in_2():
        print('this is func_in_2')
        print('this is func_in_1')
        print('this is login')
'''
'''
结果：
    print('this is func_out_1')
    print('this is func_out_2')
    print('this is func_in_2')
    print('this is func_in_1')
    print('this is login')
'''



# 类装饰器
class Func():
    def __init__(self, fn):
        self.fn = fn

    # __call__　方法可以使类的对象像函数一样调用
    def __call__(self):
        print('验证')
        self.fn()

@Func # test = Func(test)
def test():
    print('登录')

test()
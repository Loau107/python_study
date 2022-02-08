# 闭包
# 1 在函数嵌套（函数里面再定义函数）的前提下
# 2 内部函数使用了外部函数的变量（还包括外部函数的参数）
# 3 外部函数返回了内部函数

def func_out(data):
    num1 = 100
    print('外层函数1：', num1)

    def func_in():
        print(data)
        print('内层函数2：', num1)

    return func_in

func = func_out(10)
func()

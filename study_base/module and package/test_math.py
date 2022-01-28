'''
这是用于数学运算的模块
'''

def sum(a, b):
    '''计算两个参数的和\n'''
    return a + b

def sub(a, b):
    '''计算两个参数的差\n'''
    return a - b

def max(a, b):
    '''获取两个参数的最大值\n'''
    return a if a > b else b

def min(a, b):
    '''获取两个参数的最小值\n'''
    return a if a < b else b

# __name__ 获取当前的函数名，如果是直接调用，则返回 '__main__'
if __name__ == '__main__':
    print('这是内部测试代码')
else:
    print('我被外部调用了')
    print('\n\n------------------------')
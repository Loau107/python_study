if __name__ == '__main__':
    print('内部测试')
else:
    print('module_a 被调用')

def a():
    print('module_a 中的 a() 被调用')
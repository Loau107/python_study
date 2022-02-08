def func():
    for i in range(10):
        # 当函数内出现　yield　关键字时　此函数变成一个李自成器
        yield i # 相当于 return　每执行一次 next() 返回一次 i 的值


# 通过 func 创建生成器 a
a = func()
print(next(a)) # 0
print(next(a)) # 1
for i in a: # 2 - 9
    print(i)
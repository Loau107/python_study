# 自定义模块
# import test_math
# 调用模块内的函数
# print(test_math.sum(3, 5))
# __doc__获取模块、类、函数的介绍
# print(test_math.__doc__)
# print(test_math.max.__doc__)

# 导入模块
# import 倒入
# import math, os # 导入多个模块
# import math as m # 导入模块并设置别名
# from ... import ... 导入，调用时不用通过模块名调用
# from math import pi, sin # 导入模块中的变量、函数等
# from math import * # 导入模块中的全部内用

# 动态导入
# 动态导入一般为系统内部操作
# 用__import__函数动态导入
# m = __import__('math')
# print(m.pi)
# 用 improtlib 模块进行动态导入
# import importlib
# m = importlib.import_module('math')
# print(m.pi)

# 模块加载
# 模块无论导入多少次，都只会加载一次
# import test_math
# import test_math
# import test_math
# import importlib
# importlib.reload(test_math) # importlib.reoad() 函数可以重新加载模块

# 包
# import mypackage.module_a, mypackage.mypack.module_aa
# from mypackage import * # 导入包内 __init__.py 中 __all__ 设置的模块
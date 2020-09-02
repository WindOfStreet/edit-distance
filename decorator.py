import time
from functools import wraps

# 打印程序运行时长
class PrintTime:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        t1 = time.process_time()
        result = self.__func(*args, **kwargs)
        t2 = time.process_time()
        print('函数运行{}秒。'.format(t2 - t1))
        return result


# 成员函数的方法还未成功，有时间再继续尝试下
class Decorator:
    def print_time(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''count running time'''
            t1 = time.process_time()
            func(*args, **kwargs)
            t2 = time.process_time()
            print('函数运行{}秒。'.format(t2 - t1))
        return wrapper

    #
    # def print_time(self, *args, **kwargs):
    #     t1 = time.process_time()
    #     result = self.__func(*args, **kwargs)
    #     t2 = time.process_time()
    #     print('函数运行{}秒。'.format(t2 - t1))
    #     return result
import time
import random

def decorator_1(func):
    def task3(*args, **kwargs):
        starting = time.time()
        result = func(*args, **kwargs)
        ending = time.time()
        executionn = ending - starting
        print(f"{func.__name__} call executed in {executionn:.4f} sec")
        return result
    return task3

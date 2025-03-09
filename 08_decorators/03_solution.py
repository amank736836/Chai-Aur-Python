import time


def cache(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        print(cache)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print(long_running_function(1, 2))
print(long_running_function(2, 3))
print(long_running_function(1, 2))
print(long_running_function(2, 3))

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {round(end - start,2)} seconds for {func.__name__}")
        return result

    return wrapper


@timer
def amanCoder(num):
    time.sleep(2)
    def aman(x):
        return x**num
    return aman


myResult = amanCoder(2)
print(myResult(3))

def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ", ".join(str(arg) for arg in args)
        kwargs_values = ", ".join(f"{key}={value}" for key, value in kwargs.items())
        all_values = ", ".join(filter(None, [args_values, kwargs_values]))
        print(f"Calling {func.__name__}({all_values})")
        # print(
        #     f"Calling {func.__name__} with args: {args_values} and kwargs: {kwargs_values}"
        # )
        return func(*args, **kwargs)

    return wrapper


@debug
def greet(name, message="Hello"):
    return f"{message} {name}"


print(greet("Aman", "Hi"))
print(greet("Aman"))

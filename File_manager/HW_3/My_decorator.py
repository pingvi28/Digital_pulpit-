def print_func_result_decorator(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


@print_func_result_decorator
def simple_func_sum(a, b):
    return a + b


simple_func_sum(4, 5)

import time

def is_time(func):
    def wrapper(*args, **kwargs):
        """Имеем время выполнение функции"""
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"функция {func.__name__} выполнилась за {end - start:.6f} секунд")
        return result
    return wrapper

@is_time
def sum_numbers(numbers):
    return sum(numbers)

res = sum_numbers(range(1000000000000))
print(res)

@is_time
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Nikita")
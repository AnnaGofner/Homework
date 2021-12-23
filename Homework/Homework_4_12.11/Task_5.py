from functools import reduce

numbers = [n for n in range(100, 1001) if n % 2 == 0]
def mul_func(a, b):
    return a * b
print(reduce(mul_func, numbers))
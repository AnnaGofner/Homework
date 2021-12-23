def my_func(a, b, c):
    numbers = [a, b, c]
    min_1 = min(numbers)
    numbers.remove(min_1)
    result = sum(numbers)
    print(result)

my_func(-8, 7, 1)

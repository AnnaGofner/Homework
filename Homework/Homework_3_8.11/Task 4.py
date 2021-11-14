def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if x <= 0:
        return "X must be more than 0"
    if y >= 0:
        return "Y must be less then 0"
    else:
        return 1 / result

print(my_func(float(2), int(-2)))


def my_func(x, y):
    if x <= 0:
        return "X must be more than 0"
    if y >= 0:
        return "Y must be less than 0"
    return x**y

print(my_func(float(2), int(-2)))
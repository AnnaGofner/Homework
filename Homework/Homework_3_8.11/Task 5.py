def sum_func(numbers, stop):
    numbers = numbers.split()
    result = 0
    for elem in numbers:
        if elem == stop:
            break
        result += int(elem)
    return result

stop = 's'
finished = False
result = 0
while not finished:
    user_num = input("Введите числа через пробел или s для выхода: ")
    result += sum_func(user_num, stop)
    finished = stop in user_num
    print(f"Сумма равна: {result}")

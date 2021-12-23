def div_func(arg_1, arg_2):
    try:
        result = arg_1 / arg_2
        return result
    except ZeroDivisionError:
        return "Дурачок, делить на 0 нельзя!"

print(div_func(arg_1=float(input("Введите число: ")), arg_2=float(input("Введите число: "))))
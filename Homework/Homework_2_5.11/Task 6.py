while input("Добавить новый товар. Да/Нет : ") == "Да":
    n = int(input("Введите номер товара: "))
    my_dict_1 = dict(название=input("Введите название товара: "), цена=input("Введите цену товара: "), количество=input("Введите количество товара: "), ед=input("Введите единицу измерения: "))
    tuple([n, my_dict_1])
print(tuple([n, my_dict_1]))
# print(my_dict_1.values())
# print(f"Название: {my_dict_1.values(1)}")

# my_tuple_1 = tuple({"название": input("Введите название товара")})
# print(my_tuple_1)

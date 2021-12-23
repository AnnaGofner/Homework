goods = []
while input("Добавить новый товар. Да/Нет : ") == "Да":
    n = int(input("Введите номер товара: "))
    my_dict_1 = dict(название=input("Введите название товара: "), цена=int(input("Введите цену товара: ")), количество=int(input("Введите количество товара: ")), ед=input("Введите единицу измерения: "))
    goods.append(tuple([n, my_dict_1]))
for elem in goods:
    print(elem)
analit = {}
for elem in goods:
    for key, value in elem[1].items():
        if key in analit:
            analit[key].append(value)
        else:
         analit[key] = [value]
for key in analit:
    print(key, analit[key])

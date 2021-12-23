n = int(input('Введите месяц в виде целого число от 1 до 12: '))
seasons_list = ['весна', 'лето', 'осень', 'зима']
seasons_dict = {1: "весна", 2: "лето", 3: "осень", 4: "зима"}
if n == 3 or n == 4 or n == 5:
    print(f"Время года: {seasons_list[0]}")
    print(f"Время года: {seasons_dict.get(1)}")
elif n == 6 or n == 7 or n == 8:
    print(f"Время года: {seasons_list[1]}")
    print(f"Время года: {seasons_dict.get(2)}")
elif n == 9 or n == 10 or n == 11:
    print(f"Время года: {seasons_list[2]}")
    print(f"Время года: {seasons_dict.get(3)}")
elif n == 12 or n == 1 or n == 2:
    print(f"Время года: {seasons_list[3]}")
    print(f"Время года: {seasons_dict.get(4)}")

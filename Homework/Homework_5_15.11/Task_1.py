with open('task1.txt', 'w') as file_obj:
    content = input('Введите данные: \n')
    while content:
        file_obj.write(f"{content}\n")
        content = input('Введите данные: \n')
str_1 = list(input("Введите строку из нескольких слов через пробел: ").split())
for elem in range(len(str_1)):
    print(str(elem+1) + " " + str_1[elem][0:10])

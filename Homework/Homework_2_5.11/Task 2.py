list_1 = list(input('Введите слово: '))
print(list_1)
print(len(list_1))
if len(list_1) % 2 == 0:
    i = 0
    while i < len(list_1):
        elem = list_1[i]
        list_1[i] = list_1[i+1]
        list_1[i+1] = elem
        i += 2
else:
    i = 0
    while i < len(list_1)-1:
        elem = list_1[i]
        list_1[i] = list_1[i+1]
        list_1[i+1] = elem
        i += 2
print(list_1)

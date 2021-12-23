list_1 = [1, 5, 2.5, 'word', True, None, {}]
print(list_1)
print(list(map(type, list_1)))
for elem in list_1:
    print(f'{elem} - {type(elem)}')

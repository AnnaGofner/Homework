import random

with open('task5.txt', 'w') as file:
    for _ in range(30):
        file.write(f'{random.randint(0, 10)} ')

with open('task5.txt') as file:
    n_str = file.read().split()
    sum = 0
    for n in n_str:
        sum += int(n)

print(sum)
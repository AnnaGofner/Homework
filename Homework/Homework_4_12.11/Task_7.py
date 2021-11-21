from itertools import count
from math import factorial

def fact_func():
    for el in count(1):
        yield factorial(el)

gen = fact_func()
x = 0
for i in gen:
    if x < 12:
        print(i)
        x += 1
    else:
        break
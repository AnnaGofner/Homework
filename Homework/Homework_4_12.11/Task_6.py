from itertools import cycle, count

n = 200
numbers = [a for a in range(4)]
counter = count()
cycler = cycle(numbers)
print([next(counter) for a in range(n)])
print([next(cycler) for a in range(n)])
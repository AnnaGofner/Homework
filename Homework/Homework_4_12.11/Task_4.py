numbers = [3, 8, 12, 14, 7, 23, 18, 109, 14, 7, 20, 20]
result = [n for n in numbers if numbers.count(n) == 1]
print(result)
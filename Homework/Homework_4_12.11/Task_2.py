numbers = [12, 3, 18, 5, 213, 100, 14, 20]
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
print(result)
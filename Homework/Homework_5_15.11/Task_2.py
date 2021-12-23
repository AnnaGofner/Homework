with open('task2.txt') as file_obj:
    lines = file_obj.readline()
    count = 0
    for n, line in enumerate(lines):
        count += 1
        w_count = len(line.split())
        print(f'Строка {n +1} содержит {w_count} слов.')
    print(f"Файл содержит {count} строк.")
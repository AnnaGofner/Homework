result = {}
with open('task6.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        hours = 0
        for el in data[1:]:
            if el != '-':
                n = 0
                for i in el:
                    if i.isdigit():
                        n += 1
                    else:
                        break
                hours += int(n)
        result.update({data[0].strip(':'): hours})
print(result)
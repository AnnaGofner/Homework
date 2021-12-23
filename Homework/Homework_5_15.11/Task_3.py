with open('task3.txt') as file:
    file_lines = file.readlines()
    emp = {}
    sum_sal = 0
    for line in file_lines:
        emp_info = line.split()
        emp.update({emp_info[0]: float(emp_info[1])})
        sum_sal += float(emp_info[1])
average_sal = sum_sal / len(emp)
print(f"Средний оклад = {average_sal}")

for k, v in emp.items():
    if v < 20000:
        print(f"{k}: {v}")
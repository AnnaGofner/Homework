a = float(input("Введите результат пробежки в первый день: "))
b = float(input("Введите желаемое количество километров: "))
days = 1
km = a
while km < b:
    a = a + a * 0.1
    days = days + 1
    km = a
print(f"Желаемого результата вы достигнете через {days} дней")
time_str = input("Введите время в секундах: ")
time = int(time_str)
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Time: {hours:02}:{minutes:02}:{seconds:02}")
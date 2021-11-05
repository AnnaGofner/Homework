name = input("What is your name? ")
print(f"Hello, {name}!")

age_str = input('How old are you? ')
age = int(age_str)
if age < 18:
    print(f"You need to do your homework, {name}!")
elif age >= 18:
    sex_str = input('Enter your sex ')
    sex = str(sex_str)
    if "female" in sex:
        print(f"Drink a glass of wine, {name}!")
    else:
        print(f"Let's have a beer, {name}!")
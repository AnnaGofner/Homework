# number_str = input("Print a number: ")
# number = int(number_str)
# print(number + (number*11) + (number*111))

user_number = input("Print a number: ")
n = int(user_number)
number = (n + int(str(n) + str(n)) + int(str(n)+str(n)+str(n)))
print(number)
n = int(input("Введите число: "))
my_list = [23, 9, 4, 3, 2, 2]
c = my_list.count(n)
for elem in my_list:
    if c > 0:
        a = my_list.index(n)
        my_list.insert(a+c, n)
        break
    else:
        if n > elem:
            b = my_list.index(elem)
            my_list.insert(b, n)
            break
        elif n < my_list[len(my_list) - 1]:
            my_list.append(n)
print(my_list)

# my_list = [23, 9, 4, 3, 2, 2]
# n = int(input("Введите число: "))
# if n <= 2:
#     my_list.insert(6, n)
#     print(my_list)
# elif n == 3:
#     my_list.insert(4, n)
#     print(my_list)
# elif n == 4:
#     my_list.insert(3, n)
#     print(my_list)
# elif n > 4 and n <= 9:
#     my_list.insert(2, n)
#     print(my_list)
# elif n <= 23 and n > 9:
#     my_list.insert(1, n)
#     print(my_list)
# elif n > 23:
#     my_list.insert(0, n)
#     print(my_list)






def int_func(a):
    return a.title()
print(int_func("abba"))

def int_func_1(a):
    for elem in a:
        print(f"{int_func(elem)}, ")
print(int_func("today is a good day"))
def input_number():
    lst_console = input("Введите список чисел через пробел: ")
    numbers = lst_console.split(" ")
    return numbers


def first_way(orig_list):
    try:
        lst = [int(i) for i in orig_list]
        print(f"Список до: {lst}")
        print(f"    Список четных: {[i for i in lst if i % 2 == 0]}")
        print(f"    Список нечетных: {[i for i in lst if i % 2 != 0]}")
        print(f"    Список < 0: {[i for i in lst if i < 0]}")
    except ValueError:
        print(-1)
        quit()


def second_way(orig_list):
    try:
        lst = list(map(int, orig_list))
        print(f"Список до: {lst}")
        print(f"    Список четных: {list(filter(lambda x: (x % 2 == 0), lst))}")
        print(f"    Список нечетных: {list(filter(lambda x: (x % 2 != 0), lst))}")
        print(f"    Список < 0: {list(filter(lambda x: (x < 0), lst))}")
    except ValueError:
        print(-1)
        quit()


str_lst = input_number()
print("1 способ - через list comprehensions\n")
first_way(str_lst)

print("\n\n2 способ - через  map/filter\n")
second_way(str_lst)


# name = input("VV name\n")
# print("Hello world" + name)
# 1.3 --------------------------------- Оператор if / elis / else
# is_working = input("Вы работаете сейчас? 1/0") == "1"
#
# if is_working:
#     print("YES")
# else:
#     print("NO")
# 1.4 --------------------------------- Список, кортеж, словарь, множество
# # список
# lst = [1, 2, 3]
# lst.append(4)
# lst.remove(2)
# print(lst[-1])
# print(lst)
#
# lst_console = input("Введите список:\n ")
# number = lst_console.split(" ")
# print(number)
#
# # кортеж
# tup = (1,2,3)
# print(tup)
# print(tup[-1])
#
# # присвоит значения подряд
# first, second, third = tup
#
# # словарь
# en_rus_dict = {
#     "cat" : "кот",
#     "car" : "машина",
# }
#
# print(en_rus_dict['cat']) #кот
# #замена значения по ключу
# en_rus_dict['cat'] = 'кошка'
# print(en_rus_dict['cat'])
#
# # проверка на наличие
# print('car' in en_rus_dict)
#
# print(en_rus_dict.values())
# print(en_rus_dict.keys())
# # пары ключ-значение
# print(en_rus_dict.items())
#
# # зашита от дурака - если элемента, выведет None или сообщение (перегрузка)
# print(en_rus_dict.get("brother", "нет такого"))
#
# # множество
# set_from_lst = set(lst)
# set_example = {1, 2, 3}
# print(set_example)
#
# set_example.add(5)
# set_example.remove(2)
#
# print(set_example - {1, 3})
# print(set_example.union({7, 8}))
# print(set_example == {5, 6})
#
# # длинна строки
# print(len(set_example))

# 1.5 --------------------------------- Циклы

# ------------ FOR
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

en_rus_dict = {
    "cat" : "кот",
    "car" : "машина",
}

# напечатет элементы списка
# for item in lst2:
#     print(item)

# цикл завязан на генерации промежутка
# print(range(10))
# print(list(range(10)))

# значения range генерируются в процессе цикла
for i in range(10):
    if i == 1:
        continue # продолжить выполненение
    if i == 5:
        break # остановить
    print(i)

cats = ["Пушок", "Барсик", "Васька"]
# пронумеровали элементы - список с парами (индексация)
print(list(enumerate(cats)))

for ind, cat in enumerate(cats):
    print(f"{ind}, {cat}")

# возвращает итератор == надо выводить через цикл <list_reverseiterator object at 0x00000194EFCC4F40>
print(reversed(cats))

print(list(reversed(cats)))
print(list(sorted(cats)))
#------ о словаре
for key, value in en_rus_dict.items():
    print("ключ = ", key, ", значение = ", value)

# ------------ WHILE
i = 0
while i != 5:
    i += 1
print(i)

# код символа
print("a ", ord("a"))

symbol_number = ord("a")
# вывод алфавита
while symbol_number <= ord("z"):
    print(symbol_number, chr(symbol_number))
    symbol_number +=1

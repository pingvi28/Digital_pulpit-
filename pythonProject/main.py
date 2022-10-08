# Импорт модуля
# import calc as clc
#
# print(clc.addition(2,3))


# list comprehensions
# range_from_one_to_six = [i for i in range(1, 7)]
# print(range_from_one_to_six)

# map
# def foo(num):
#     return num + 1
#
# mas = list(map(foo, [i for i in range(0, 7)]))
# print(mas)
# анонимные функции (lambda) + map
# mas = list(map(lambda num: 'more' if num>2 else 'not more', [i for i in range(0, 7)]))
# print(mas)


# filter
# def foo(word):
#     return len(word) % 2 == 0
# mas = list(filter(foo, ['aa', 'bb', 'abc', 'abcd', 'abcde']))
# print(mas)
#
# # lambda filter
# mas = list(filter(lambda word: len(word) % 2 == 0, ['aa', 'bb', 'abc', 'abcd', 'abcde']))
# print(mas)

# reduce
# from functools import reduce
#
# def foo(a, b):
#     return a + b
#
# summ = reduce(foo, [i for i in range(1, 7)])
# print(summ)
# reduce + lambda
# mult = reduce(lambda num, num1: num * num1, [i for i in range(1, 7)])
# print(mult)

# annotations
# class Test:
#     def __init__(self, first: int, second: str) -> None:
#         self.first: int = first
#         self.second: str = second
#
#     def foo(self) -> str:
#         return self.first*self.second


# каррирование (не комментировалось должным образом, чекай calc)
# from calc import foo_out
#
# print(foo_out(2, False)(3))

# регулярные выражения (https://habr.com/ru/post/349860/ для изучения)
import re

# text = 'aa aab aabb aabb aaaabb aaaabbb'
# word = re.search(r'\baab\b', text) # ищет конкретный шаблон, поэтому обязательно указывать границы слова
# word = word.group()
# print(word)

text = 'aa aab aabb aabb aaaabb aaaabbb'
words = re.findall(r'\b(?:aa)+b(?:bb)*\b', text)  # (?<=) - начинается с. (?=) - заканчивается на
print(words)
words = re.findall(r'(?<=aa)\S+\b', text)
print(words)








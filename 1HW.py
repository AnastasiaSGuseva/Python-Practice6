"""
Задание 3 из домашнего задания 2:

Задайте список из n чисел последовательности 
(1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.

Пример:

Для n = 6 -> 14.072

"""


# n = int(input('Введите число: '))
# scroll = []
# sum_ = 0

# for i in range(1, n + 1):
#     scroll.append(((1 + 1/i)**i))

# for i in range(n):
#     sum_ += scroll[i]

# print(round(sum_, 3))


n = int(input('Введите число: '))

list1 = [((1+1/i)**i) for i in range(1, n+1)]
result = sum(list1)

print(round(result, 3))

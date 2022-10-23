"""
Задание 1 из домашнего задания 2:
Напишите программу, которая принимает на вход 
вещественное число и показывает сумму его цифр.

Пример:

6782 -> 23
0,56 -> 11

"""


# Number = input('Введите число: ')
# a = len(Number)
# sum_ = 0

# for i in range(a):
#     if Number[i].isdigit():
#         c = int(Number[i])
#         sum_ = sum_ + c
#     else:
#         i += 1
# print('Сумма равна', sum_)


number = input('Введите число: ')
summ = sum(list(map(int, (filter(lambda x: x.isdigit(), number)))))

print(summ)

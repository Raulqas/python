#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя ни одной из операций деления: ни деления с плавающей точкой /, ни целочисленного деления //
# и взятия остатка %
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
result = -1
prost = a
while (prost > 0):
    result += 1
    prost -= b
print('Целочисленное деление', a, 'на', b, 'дает', result)
# TODO здесь ваш код

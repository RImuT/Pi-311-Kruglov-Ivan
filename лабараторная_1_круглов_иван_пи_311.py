# -*- coding: utf-8 -*-
"""Лабараторная #1 Круглов Иван ПИ-311

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rYbUaWtggvsZ67uMinof-wnsPyNio9_t
"""

a = 5
b = int(input())
print(a*b)

a = int(input())
b = int(input())
print((a+b)**2)

a = 15
b = 10
C = int(input())
print((a+b)//C)

print('(a**2)+ 2*a*b + (b**2)')
a = int(input())
b = int(input())
print((a**2)+ 2*a*b + (b**2))

a = int(input())
b = int(input())
print((((a**3)+14)//5)*b)

a = int(input())
print(a**2)
n = int(input())
print((a**2)//n)

a = float(input())
b = float(input())
print('Деление дробных чисел без остатка', a//b)
a = float(input())
b = float(input())
print('Умножение двух натуральных чисел', a*b)
a = float(input())
b = float(input())
print('Получение остатка от деления двух натуральтных чисел', a%b)

s = int(input())
m = s //60
h = s //3600
d = h // 24
print('Дней:', d)
print('Часов:', h)
print('Минут:',m)

n = input()
a = str(n)
m1 = a + a
m2 = a + a +a
print(n+m1+m2)
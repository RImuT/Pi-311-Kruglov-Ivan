# -*- coding: utf-8 -*-
"""Лабораторная работа №6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IVg22u5P60WBvo0G-YCK6-YC7i4iS_cB
"""

celsius = [[-67.0], [-34.0],[0], [ 34.0], [54.0], [67.0], [100]]
fahrenheit = [[-88.6], [-29.2], [32.0], [93.2], [129.2], [152.6], [212.0]]

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
plt.figure(figsize=(15,8), dpi = 50)
plt.scatter(celsius, fahrenheit, label='входные значения', color = 'green', marker = '$f$');
plt.xlabel('celsius')
plt.ylabel('fahrenheit')
plt.legend()
plt.grid(True)
plt.show()

for c,f in zip(celsius, fahrenheit):
  print(f'цельсия {c} фаренгейта{f}')

lr = LinearRegression ()
lr.fit(celsius, fahrenheit)
lr.predict([[256], [123]])
lr.coef_
lr.intercept_
celsius_test = [[-50], [10], [30], [20], [10], [70], [87]]
fahrenheit_test = lr.predict(celsius_test)
fahrenheit_test

for c,f in zip(celsius_test, fahrenheit_test):
  print(f'цельсия {c} фаренгейта{f}')

import numpy as np
x_range = np.arange(-70, 120)
y_range = x_range*1.8 + 32
plt.figure(figsize=(15,8), dpi = 280)
plt.plot(x_range, y_range, label = 'уравнение', linewidth = '1')
plt.scatter(celsius, fahrenheit, label = 'уравнение', linewidth = '1')
plt.scatter(celsius_test, fahrenheit_test, label = 'предсказанное значение', color = 'blue')
plt.xlabel('Цельсия')
plt.ylabel('Фаренгейт')
plt.legend()
plt.grid(True)
plt.show()

#Задание 1
fahrenheit2 = [[-67.0],[-34.0],[0],[34.0],[54.0],[67.0],[100]]
celvin2 = [[218.1],[236.5],[255.4],[274.3],[285.4],[292.6],[310.9]]

plt.figure(figsize=(15,8), dpi=50)
plt.scatter(fahrenheit2, celvin2, label='входные данные', color='green', marker='$f$');
plt.xlabel('fahrenheit')
plt.ylabel('kelvins')
plt.legend()
plt.grid(True)
plt.show()

lr = LinearRegression()
lr.fit(fahrenheit2, celvin2)
lr.predict([[256],[123]])
lr.coef_
lr.intercept_
fahrenheit2_test = [[-50],[10],[30],[20],[10],[70],[87]]
celvin2_test = lr.predict(fahrenheit2_test)
celvin2_test

x_range = np.arange(-70,120)
y_range = x_range*1.8+32
plt.figure(figsize=(15,8), dpi=280)
plt.plot(x_range, y_range, label='уравнение', linewidth='1')
plt.scatter(fahrenheit2,celvin2, label='входные данные', color='green')
plt.scatter(fahrenheit2_test, celvin2_test, label='предсказанное значение', color='blue')
plt.xlabel('Фаренгейта')
plt.ylabel('Кельвина')
plt.legend()
plt.grid(True)
plt.show()

#Задание 2 выполнено

#Задание 3
import matplotlib.pyplot as plt
import numpy as np

index = np.arange(3)
values = [2.910,2.562,2]
plt.bar(index, values)
plt.xticks(index+0.4, ['Facebook','Youtube','WhatsApp'])
plt.xlabel('Социальные платформы')
plt.ylabel('Количество пользователей (в миллионах)')
plt.show()

from matplotlib import colors
labels = ['blue', 'red', 'green', 'black', 'white']
values = [33, 27, 20, 15, 5]
colors = ['blue', 'red', 'green', 'black', 'grey']
plt.pie(values, labels=labels, colors=colors)
plt.axis('equal')
plt.show()

x0 = np.arange(8)
y1 = np.array([1,3,4,5,4,3,2,1])
y2 = np.array([1,2,5,4,3,3,2,1])
plt.ylim(-7,7)
plt.bar(x0,y1,0.9, facecolor='g')
plt.bar(x0,-y2,0.9,facecolor='b')
plt.xticks(())
plt.grid(True)
plt.show()

#Задание 4
import math
#4.1:
print (math.e)
#4.2:
print (math.pi)
#4.3
x = float('nan')
math.isnan(x)
#4.4
print(math.factorial(11))
#4.5
num1 = 11
num2 = 225
ma = 0
for dil in range(1, num1-1):
  if num1%dil==0 and num2%dil==0:
    ma = max(ma, dil)
print(ma)
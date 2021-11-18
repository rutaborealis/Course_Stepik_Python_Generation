# 13.6
# 13.6.1
# объявление функции
def get_middle_point(x1, y1, x2, y2):
    middle_point_x = (x1 + x2) / 2
    middle_point_y = (y1 + y2) / 2
    return middle_point_x, middle_point_y


# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

# 13.6.2
from math import *


# объявление функции
def get_circle(radius):
    c = 2 * pi * radius
    s = pi * r ** 2
    return c, s


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)

# 13.6.3
from math import *


# объявление функции
def solve(a, b, c):
    d = b ** 2 - (4 * a * c)

    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
    elif d == 0:
        x1 = -b / (2 * a)
        x2 = -b / (2 * a)
    else:
        print('Нет корней')

    return min(x1, x2), max(x1, x2)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)

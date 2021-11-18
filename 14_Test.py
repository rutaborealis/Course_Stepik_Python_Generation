# 14 Test
# 14.1
# объявление функции
def draw_triangle():
    star = 1
    space = 7
    for i in range(8):
        print((' ' * space) + ('*' * star), sep='')
        star = star + 2
        space = space - 1


# основная программа
draw_triangle()  # вызов функции


# 14.2
# объявление функции
def get_shipping_cost(quantity):
    cost = 1000
    for i in range(quantity - 1):
        cost = cost + 120
    return cost


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))

# 14.3
from math import *


# объявление функции
def compute_binom(n, k):
    binom = int((factorial(n)) / (factorial(k) * (factorial(n - k))))
    return binom


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))


# 14.4
# объявление функции
def number_to_words(num):
    d = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
         10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
         16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
         40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
    if 1 <= num <= 19:
        return d[num]
    else:
        j = num % 10
        if j == 0:
            return d[num]
        else:
            i = (num // 10) * 10
            return d[i] + ' ' + d[j]


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))


# 14.5
# объявление функции
def get_month(language, number):
    ru = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август', 9: 'сентябрь',
          10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
    en = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
          9: 'september', 10: 'october', 11: 'november', 12: 'december'}

    if language == 'ru':
        return ru[number]
    elif language == 'en':
        return en[number]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))


# 14.6
# объявление функции
def is_magic(date):
    date_list = date.split('.')
    prod = int(date_list[0]) * int(date_list[1])
    year = int(date_list[2][2:])
    if prod == year:
        return True
    else:
        return False


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))


# 14.7
# объявление функции
def is_pangram(text):
    text = text.lower()
    text = text.replace(' ', '')
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in abc:
        if i not in text:
            return False
            break
    return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))

# 2.5
# "ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ"         "ОСТАТОК ОТ ДЕЛЕНИЯ"                          "КАК ЭТО РАБОТАЕТ"
# 19 // 5 = 3                     19 % 5 = 4                     ==>>           19 - (5 * 3) = 4
# 19 // -5 = -4                   19 % -5 = -1                   ==>>           19 - (-5 * -4) = 19 - (20) = -1
# -19 // 5 = -4                   -19 % 5 = 1                    ==>>           -19 - (5 * -4) = -19 - (-20) = -19 + 20 = 1
# -19 // -5 = 3                   -19 % -5 = -4                  ==>>           -19 - (-5 * 3) = -19 - (-15) = -19 + 15 = -4

# 2.5.1
print('Введите параметры геометрической прогрессии:')
b1 = int(input())
q = int(input())
n = int(input())

bn = b1 * (q ** (n - 1))

print('N-й член заданной геометрической прогрессии:')
print(bn)
print()

# 2.5.2
print('Введите количество сантиметров:')
a = int(input())

b = a // 100

print('Полное количество метров в введенных сантиметрах:')
print(b)
print()

# 2.5.3
print('Введите количество школьников и мандаринов:')
n = int(input())
k = int(input())

x1 = k // n
x2 = k % n

print('Количество мандаринов, которое достанется каждому мальчику:')
print(x1)
print('Количество мандаринов, которое останется:')
print(x2)
print()

# 2.5.4
print('Введите население Вселенной:')
n = int(input())

x = n % 2
if x == 0:
    population = int(n / 2)
else:
    population = int((n + 1) / 2)

print('Оставшееся население:', population)
print()

# 2.5.5
print('Введите номер места:')
n = int(input())

x = n % 4

if x == 0:
    n = n // 4
    print('Ваш вагон №:', n)
else:
    n = n // 4
    n = n + 1
    print('Ваш вагон №:', n)
print()

# 2.5.6
print('Введите количество минут:')
n = int(input())
hours = n // 60
minutes = n % 60
print(n, 'мин - это', hours, 'час', minutes, 'минут.')

# 2.5.7
print('Введите трехзначное, целое, положительное число:')
num = int(input())

last_digit = (num % (10 ** 1)) // 10 ** 0
middle_digit = (num % (10 ** 2)) // 10
first_digit = (num % (10 ** 3)) // 10 ** 2

sum = first_digit + middle_digit + last_digit
prod = first_digit * middle_digit * last_digit

print('Сумма цифр =', sum)
print('Произведение цифр =', prod)
print()

# 2.5.8
# abc, acb, bac, bca, cab, cba
print('Введите трехзначное, целое, положительное число:')
num = int(input())

c = (num % (10 ** 1)) // 10 ** 0
b = (num % (10 ** 2)) // 10
a = (num % (10 ** 3)) // 10 ** 2

num1 = (a * 100) + (c * 10) + b
num2 = (b * 100) + (a * 10) + c
num3 = (b * 100) + (c * 10) + a
num4 = (c * 100) + (a * 10) + b
num5 = (c * 100) + (b * 10) + a

print(num)
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print()

# 2.5.9
print('Введите четырехзначное, целое, положительное число:')
num = int(input())

first_digit = (num % (10 ** 4)) // 10 ** 3
second_digit = (num % (10 ** 3)) // 10 ** 2
third_digit = (num % (10 ** 2)) // 10 ** 1
fourth_digit = (num % (10 ** 1)) // 10 ** 0

print('Цифра в позиции тысяч равна', first_digit)
print('Цифра в позиции сотен равна', second_digit)
print('Цифра в позиции десятков равна', third_digit)
print('Цифра в позиции единиц равна', fourth_digit)
print()

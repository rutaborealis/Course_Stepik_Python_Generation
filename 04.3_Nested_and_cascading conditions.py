# 4.3
# 4.3.1
n = int(input())  # Zoom
k = int(input())  # Flash

if n > k:
    print('NO')
elif n < k:
    print('YES')
else:
    print("Don't know")

# 4.3.2
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Равносторонний')
elif (a == b) or (b == c) or (a == c):
    print('Равнобедренный')
else:
    print('Разносторонний')

# 4.3.3
a = int(input())
b = int(input())
c = int(input())

max = a
if b > max:
    max = b
if c > max:
    max = c

min = a
if b < min:
    min = b
if c < min:
    min = c

middle = 0
if min < a < max:
    middle = a
elif min < b < max:
    middle = b
elif min < c < max:
    middle = c

print(middle)

# 4.3.4
month = int(input())

days = 28
if ((month != 2) and (1 <= month <= 7) and (month % 2 != 0)) or (
        (month != 2) and (8 <= month <= 12) and (month % 2 == 0)):
    days = 31
elif ((month != 2) and (2 < month <= 6) and (month % 2 == 0)) or (
        (month != 2) and (9 <= month <= 11) and (month % 2 != 0)):
    days = 30

print(days)

# 4.3.5
weight = int(input())

if weight < 60:
    print('Легкий вес')
elif 60 <= weight < 64:
    print('Первый полусредний вес')
elif 64 <= weight <= 69:
    print('Полусредний вес')

# 4.3.6
a = int(input())
b = int(input())
action = input()

if action == '+':
    result = int(a + b)
elif action == '-':
    result = int(a - b)
elif action == '*':
    result = int(a * b)
elif action == '/':
    if b != 0:
        result = a / b
    else:
        result = 'На ноль делить нельзя!'
else:
    result = 'Неверная операция'

print(result)

# 4.3.7
color1 = input()
color2 = input()

if ((color1 == 'красный') and (color2 == 'синий')) or ((color2 == 'красный') and (color1 == 'синий')):
    result = 'фиолетовый'
elif ((color1 == 'красный') and (color2 == 'желтый')) or ((color2 == 'красный') and (color1 == 'желтый')):
    result = 'оранжевый'
elif ((color1 == 'синий') and (color2 == 'желтый')) or ((color2 == 'синий') and (color1 == 'желтый')):
    result = 'зеленый'
elif (color1 == 'красный') and (color2 == 'красный'):
    result = 'красный'
elif (color1 == 'желтый') and (color2 == 'желтый'):
    result = 'желтый'
elif (color1 == 'синий') and (color2 == 'синий'):
    result = 'синий'
else:
    result = 'ошибка цвета'

print(result)

# 4.3.8
number = int(input())

if (number < 0) or (number > 36):
    result = 'ошибка ввода'
elif number == 0:
    result = 'зеленый'
elif (1 <= number <= 10) and (number % 2 != 0):
    result = 'красный'
elif (1 <= number <= 10) and (number % 2 == 0):
    result = 'черный'
elif (11 <= number <= 18) and (number % 2 != 0):
    result = 'черный'
elif (11 <= number <= 18) and (number % 2 == 0):
    result = 'красный'
elif (19 <= number <= 28) and (number % 2 != 0):
    result = 'красный'
elif (19 <= number <= 28) and (number % 2 == 0):
    result = 'черный'
elif (29 <= number <= 36) and (number % 2 != 0):
    result = 'черный'
elif (29 <= number <= 36) and (number % 2 == 0):
    result = 'красный'

print(result)

# 4.3.9
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if min(b1, b2) < max(a1, a2):
    print('пустое множество')
elif min(b1, b2) == max(a1, a2):
    print(min(b1, b2))
else:
    print(max(a1, a2), min(b1, b2))

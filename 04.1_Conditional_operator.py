# 4.1
# 4.1.1
password = input()
password_confirmation = input()

if password == password_confirmation:
    print('Пароль принят')
else:
    print('Пароль не принят')

# 4.1.2
num = int(input())

if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

# 4.1.3
num = int(input())

first_digit = (num % (10 ** 4)) // 10 ** 3
second_digit = (num % (10 ** 3)) // 10 ** 2
third_digit = (num % (10 ** 2)) // 10 ** 1
fourth_digit = (num % (10 ** 1)) // 10 ** 0

if first_digit + fourth_digit == second_digit - third_digit:
    print('ДА')
else:
    print('НЕТ')

# 4.1.4
age = int(input())

if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

# 4.1.5
a1 = int(input())
a2 = int(input())
a3 = int(input())

d1 = (a2 - a1) / (2 - 1)
d2 = (a3 - a1) / (3 - 1)

if d1 == d2:
    print('YES')
else:
    print('NO')

# 4.1.6
a = int(input())
b = int(input())

minimum = a

if a < b:
    minimum = a
else:
    minimum = b

print(minimum)

# 4.1.7
a = int(input())
b = int(input())
c = int(input())
d = int(input())

minimum = a

if a < b:
    minimum = a
else:
    minimum = b

if minimum < c:
    minimum = minimum
else:
    minimum = c

if minimum < d:
    minimum = minimum
else:
    minimum = d

print(minimum)

# 4.1.8
# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.
age = int(input())

if age <= 13:
    print('детство')
elif 14 <= age <= 24:
    print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
elif age >= 60:
    print('старость')

# 4.1.9
a = int(input())
b = int(input())
c = int(input())

sum_positive = 0

if a > 0:
    sum_positive = sum_positive + a

if b > 0:
    sum_positive = sum_positive + b

if c > 0:
    sum_positive = sum_positive + c

print(sum_positive)

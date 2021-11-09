# 6.1
# 6.1.1
a = float(input())
b = float(input())
c = 0.5

s = float(c * a * b)

print(s)

# 6.1.2
# s = v1 * t1
# s = v2 * t2
# t1 = s / v1
# t2 = s / v2
# t = s / (v1 + v2)
s = float(input())
v1 = float(input())
v2 = float(input())

t = float(s / (v1 + v2))

print(t)

# 6.1.3
num = float(input())

if num == 0:
    result = 'Обратного числа не существует'
else:
    result = float(1 / num)

print(result)

# 6.1.4
tempreture_f = float(input())
tempreture_c = float(5 / 9 * (tempreture_f - 32))
print(tempreture_c)

# 6.1.5
n = float(input())

if n <= 2:
    age_human = (n * 10.5)
else:
    n1 = float(n - 2)
    age_human = (2 * 10.5 + (n1 * 4))

print(age_human)

# 6.1.6
n = float(input())
n1 = int(n)

dif = int((n - n1) * 10)
print(dif)

# 6.1.7
n = float(input())
n1 = int(n)
dif = n - n1
print(dif)

# 6.1.8
a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
minimum = min(a, b, c, d, e)
maximum = max(a, b, c, d, e)

print('Наименьшее число =', minimum)
print('Наибольшее число =', maximum)

# 6.1.9
a, b, c = int(input()), int(input()), int(input())

minimum = min(a, b, c)
maximum = max(a, b, c)
middle = (a + b + c) - (minimum + maximum)

print(maximum)
print(middle)
print(minimum)

# 6.1.10
num = int(input())

last_digit = (num % (10 ** 1)) // 10 ** 0
middle_digit = (num % (10 ** 2)) // 10
first_digit = (num % (10 ** 3)) // 10 ** 2

maximum = max(last_digit, middle_digit, first_digit)
minimum = min(last_digit, middle_digit, first_digit)

dif = maximum - minimum
middle = (first_digit + middle_digit + last_digit) - (minimum + maximum)

if dif == middle:
    result = 'Число интересное'
else:
    result = 'Число неинтересное'

print(result)

# 6.1.11
a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
sum = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
print(sum)

# 6.1.12
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
s = abs(p1 - q1) + abs(p2 - q2)
print(s)

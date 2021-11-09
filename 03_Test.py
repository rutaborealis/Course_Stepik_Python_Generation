# 3 Test
# 3.1
print('*****************')
print('*               *')
print('*               *')
print('*****************')
print()

# 3.2
a = int(input())
b = int(input())

square_of_the_sum = (a + b) ** 2
sum_of_squares = (a ** 2) + (b ** 2)

print('Квадрат суммы', a, 'и', b, 'равен', square_of_the_sum)
print('Сумма квадратов', a, 'и', b, 'равна', sum_of_squares)

# 3.3
a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = (a ** b) + (c ** d)

print(x)

# 3.4
n = int(input())

if n // 1 == 1:
    x = n + ((n * 10) + 1) + ((n * 100) + (n * 10) + 1)
else:
    x = n + ((n * 10) + n) + ((n * 100) + (n * 10) + n)

print(x)

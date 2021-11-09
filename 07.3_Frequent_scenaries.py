# 7.3
# 7.3.1
a, b = int(input()), int(input())
counter = 0

for i in range(a, b + 1):
    cube = i ** 3
    end = cube % 10
    if (end == 4) or (end == 9):
        counter = counter + 1

print(counter)

# 7.3.2
n = int(input())
sum = 0

for i in range(n):
    num = int(input())
    sum = sum + num

print(sum)

# 7.3.3
from math import *

n = int(input())
sum = 0

for i in range(1, n + 1):
    sum = sum + (1 / i)

total = sum - log(n)

print(total)

# 7.3.4
n = int(input())
sum = 0

for i in range(1, n + 1):
    square = i ** 2
    end = square % 10
    if (end == 2) or (end == 5) or (end == 8):
        sum = sum + i

print(sum)

# 7.3.5
n = int(input())
mult = 1

for i in range(1, n + 1):
    mult = mult * i

print(mult)

# 7.3.6
mult = 1
for i in range(10):
    n = int(input())
    if n != 0:
        mult = mult * n

print(mult)

# 7.3.7
n = int(input())
sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        sum = sum + i

print(sum)

# 7.3.8
n = int(input())
sum = 0
flag = True

for i in range(1, n + 1):
    if flag == True:
        sum = sum + i
        flag = False
    else:
        sum = sum - i
        flag = True

print(sum)

# 7.3.9
n = int(input())
largest = 0
pre_largest = 0

for i in range(1, n + 1):
    number = int(input())
    if number > largest:
        pre_largest = largest
        largest = number
    elif number < largest:
        if number > pre_largest:
            pre_largest = number

print(largest)
print(pre_largest)

# 7.3.10
flag = True

for i in range(10):
    num = int(input())
    if num % 2 != 0:
        flag = False

if flag:
    print('YES')
else:
    print('NO')

# 7.3.11
# Последовательность Фибоначчи
n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

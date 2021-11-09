# 5 Test
# 5.1
year = int(input())

if year % 100 == 0:
    print('YES')
else:
    print('NO')

# 5.2
# Имеют ли указанные клетки один цвет или нет
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if ((x1 + y1) % 2 == 0) and ((x2 + y2) % 2 == 0):
    print('YES')
elif ((x1 + y1) % 2 != 0) and ((x2 + y2) % 2 != 0):
    print('YES')
else:
    print('NO')

# 5.3
age = int(input())
sex = input()

if 10 <= age <= 15:
    if sex == 'f':
        result = 'YES'
    else:
        result = 'NO'
else:
    result = 'NO'

print(result)

# 5.4
number = int(input())

if (number < 1) or (number > 10):
    result = 'ошибка'
elif number == 1:
    result = 'I'
elif number == 2:
    result = 'II'
elif number == 3:
    result = 'III'
elif number == 4:
    result = 'IV'
elif number == 5:
    result = 'V'
elif number == 6:
    result = 'VI'
elif number == 7:
    result = 'VII'
elif number == 8:
    result = 'VIII'
elif number == 9:
    result = 'IX'
elif number == 10:
    result = 'X'

print(result)

# 5.5
n = int(input())

if n % 2 != 0:
    print('YES')
elif (n % 2 == 0) and (2 <= n <= 5):
    print('NO')
elif (n % 2 == 0) and (6 <= n <= 20):
    print('YES')
elif (n % 2 == 0) and (n > 20):
    print('NO')

# 5.6
# Ход слона
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')

# 5.7
# Ход коня
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')

# 5.8
# Ход ферзя
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

diagonal_1 = (x1 + y1 == x2 + y2)
diagonal_2 = (x1 + y2 == y1 + x2)
vertical = (y1 == y2)
horizontal = (x1 == x2)

if diagonal_1 or diagonal_2 or vertical or horizontal:
    print("YES")
else:
    print("NO")

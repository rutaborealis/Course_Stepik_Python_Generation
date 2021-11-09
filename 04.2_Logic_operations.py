# 4.2
# 4.2.1
x = int(input())

if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

# 4.2.2
x = int(input())

if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

# 4.2.3
x = int(input())

if (-30 < x <= -2) or (7 < x <= 25):
    print('Принадлежит')
else:
    print('Не принадлежит')

# 4.2.4
x = int(input())

if (1000 <= x <= 9999 or -9999 <= x <= -1000) and ((x % 7 == 0) or (x % 17 == 0)):
    print('YES')
else:
    print('NO')

# 4.2.5
a = int(input())
b = int(input())
c = int(input())

# Теорема невырожденного треугольника
if (a < b + c) and (b < a + c) and (c < a + b):
    print('YES')
else:
    print('NO')

# 4.2.6
year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('YES')
else:
    print('NO')

# 4.2.7
# Ход ладьи
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())

if (x1 == x) or (y1 == y):
    print('YES')
else:
    print('NO')

# 4.2.7
# Ход короля
x = int(input())
y = int(input())
x_user = int(input())
y_user = int(input())

x1 = x + 1
x2 = x - 1
y1 = y + 1
y2 = y - 1

if (x_user == x and y_user == y1) or (x_user == x1 and y_user == y1) or (x_user == x1 and y_user == y) or (
        x_user == x1 and y_user == y2) or (x_user == x and y_user == y2) or (x_user == x2 and y_user == y2) or (
        x_user == x2 and y_user == y) or (x_user == x2 and y_user == y1):
    print('YES')
else:
    print('NO')

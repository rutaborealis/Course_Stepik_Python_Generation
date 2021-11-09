# 7.2
# 7.2.1
n, m = int(input()), int(input())
for i in range(n, m + 1):
    print(i)

# 7.2.2
n, m = int(input()), int(input())

if n < m:
    for i in range(n, m + 1):
        print(i)
else:
    for i in range(n, m - 1, -1):
        print(i)

# 7.2.3
n, m = int(input()), int(input())
for i in range(n, m - 1, -1):
    if i % 2 != 0:
        print(i)

# 7.2.4
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif (i % 3 == 0) and (i % 5 == 0):
        print(i)

# 7.2.5
n = int(input())
for i in range(1, 11):
    result = n * i
    print(n, 'x', i, '=', result)

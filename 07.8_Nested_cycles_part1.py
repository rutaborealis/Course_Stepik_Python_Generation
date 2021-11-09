# 7.8
# 7.8.1
# решение 1
n = int(input())

for i in range(n):
    for j in range(3):
        print(n, end=" ")
    print()

# решение 2
n = input()
string = (n + ' ') * 3
n = int(n)

for i in range(n):
    print(string)

# 7.8.2
n = int(input())

for i in range(1, n + 1):
    for j in range(5):
        print(i, end=" ")
    print()

# 7.8.3
n = int(input())

for i in range(1, n + 1):
    for j in range(1, 10):
        sum = i + j
        print(i, '+', j, '=', sum)
    print()

# 7.8.4
n = int(input())
mid = n // 2 + 1

for i in range(1, n + 1):
    if i <= mid:
        print('*' * i)
    else:
        print('*' * (n - i + 1))

# 7.8.5
n = int(input())

for i in range(1, n + 1):
    n = i
    i = str(i)
    print(i * n)

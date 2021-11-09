# 7.1
# 7.1.1
for i in range(10):
    print('Python is awesome!')

# 7.1.2
sentence = input()
n = int(input())

for i in range(n):
    print(sentence)

# 7.1.3
for i in range(6):
    print('AAA')

for i in range(5):
    print('BBBB')
print('E')

for i in range(9):
    print('TTTTT')
print('G')

# 7.1.4
b = int(input())
a = '*' * 19

for i in range(b):
    print(a)

# 7.1.5
a = input()

for i in range(10):
    print(i, a)

# 7.1.6
n = int(input())

print('Квадрат числа 0 равен 0')

for i in range(n):
    print('Квадрат числа', i + 1, 'равен', (i + 1) ** 2)

# 7.1.7
n = int(input())
a = '*'

for i in range(n):
    result = a * n
    print(result)
    n = n - 1

# 7.1.8
population = float(input())
p = float(input())
n = int(input())

for i in range(n):
    i = i + 1
    print(i, population)
    population = population + (population * p / 100)

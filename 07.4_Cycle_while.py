# 7.4
# 7.4.1
sentence = input()

while sentence != 'КОНЕЦ':
    print(sentence)
    sentence = input()

# 7.4.2
sentence = input()

while sentence != 'КОНЕЦ' and sentence != 'конец':
    print(sentence)
    sentence = input()

# 7.4.3
text = input()
sum = 0

while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    sum = sum + 1
    text = input()

print(sum)

# 7.4.4
n = int(input())

while n % 7 == 0:
    print(n)
    n = int(input())

# 7.4.5
num = int(input())
sum = 0

while num >= 0:
    sum = sum + num
    num = int(input())

print(sum)

# 7.4.6
num = int(input())
counter = 0

while (num > 0) and (num <= 5):
    if num == 5:
        counter = counter + 1
    num = int(input())

print(counter)

# 7.4.7
n = int(input())
i = 0

while n >= 25:
    n -= 25
    i += 1
while n >= 10:
    n -= 10
    i += 1
while n >= 5:
    n -= 5
    i += 1
while n >= 1:
    n -= 1
    i += 1

print(i)

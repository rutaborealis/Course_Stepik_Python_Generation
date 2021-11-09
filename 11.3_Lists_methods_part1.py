# 11.3
# 11.3.1
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
           12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if (5 in numbers) and (17 in numbers):
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

# 11.3.2
n = int(input())
list = []

for i in range(n):
    string = input()
    list.append(string)

print(list)

# 11.3.3
alphabet = []
count = 1

for i in range(97, 123):
    element = chr(i) * count
    alphabet.append(element)
    count += 1

print(alphabet)

# 11.3.4
n = int(input())
list = []

for i in range(n):
    digit = int(input())
    digit = digit ** 3
    list.append(digit)

print(list)

# 11.3.5
n = int(input())
list = []

for i in range(1, n + 1):
    if n % i == 0:
        list.append(i)

print(list)

# 11.3.6
n = int(input())
list = []
list_sum = []

for i in range(n):
    digit = int(input())
    list.append(digit)

for j in range(1, len(list)):
    sum = list[j - 1] + list[j]
    list_sum.append(sum)

print(list_sum)

# 11.3.7
n = int(input())
list = []

for i in range(n):
    digit = int(input())
    list.append(digit)

list_even_index = list[0::2]

print(list_even_index)

# 11.3.8
n = int(input())
list = []

for i in range(n):
    string = input()
    list.append(string)

k = int(input())
k = k - 1

for element in list:
    if k >= len(element):
        continue
    else:
        print(element[k], end='')

# 11.3.9
n = int(input())
list = []

for i in range(n):
    string = input()
    list.extend(string)

print(list)

# 11.4
# 11.4.1
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
sum = 0

for element in numbers:
    element = element ** 2
    sum = sum + element

print(sum)

# 11.4.2
n = int(input())
list1 = []

for i in range(n):
    digit = int(input())
    list1.append(digit)

print(*list1, sep='\n')
print()

list2 = []
for element in list1:
    result = (element ** 2) + (2 * element) + 1
    list2.append(result)

print(*list2, sep='\n')

# 11.4.3
# решение 1
n = int(input())
list = []

for i in range(n):
    digit = int(input())
    list.append(digit)

maximum = max(list)
minimum = min(list)
list1 = []

for element in list:
    if element == maximum or element == minimum:
        continue
    else:
        list1.append(element)

print(*list1, sep='\n')

# решение 2
n = int(input())
list = []

for i in range(n):
    digit = int(input())
    list.append(digit)

maximum = max(list)
minimum = min(list)

list.remove(maximum)
list.remove(minimum)

print(*list, sep='\n')

# 11.4.4
n = int(input())
list = []

for i in range(n):
    string = input()
    if string not in list:
        list.append(string)

print(*list, sep='\n')

# 11.4.5
n = int(input())
list = []

for i in range(n):
    string = input()
    list.append(string)

search = input()

for element in list:
    if search.lower() in element.lower():
        print(element)

# 11.4.6
n = int(input())
responses = []
for _ in range(n):
    responses.append(input())

k = int(input())
requests = []
for _ in range(k):
    requests.append(input())

for res in responses:
    for req in requests:
        if req.lower() not in res.lower():
            break
    else:
        print(res)

# 11.4.7
n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))

for element in list:
    if element < 0:
        print(element)

for element in list:
    if element == 0:
        print(element)

for element in list:
    if element > 0:
        print(element)

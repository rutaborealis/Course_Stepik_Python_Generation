# 11.6
# 11.6.1
numbers = [8, 9, 10, 11]
numbers2 = [4, 5, 6]
numbers[1] = 17
numbers.extend(numbers2)
del numbers[0]
numbers = numbers * 2
numbers.insert(3, 25)
print(numbers)

# 11.6.2
string = input()
numbers_str = string.split()
numbers_int = []

for element in numbers_str:
    element = int(element)
    numbers_int.append(element)

maximum = max(numbers_int)
minimum = min(numbers_int)

index_max = numbers_int.index(maximum)
index_min = numbers_int.index(minimum)

numbers_int[index_min], numbers_int[index_max] = numbers_int[index_max], numbers_int[index_min]

print(*numbers_int, sep=' ')

# 11.6.3
string = input()
string_lower = string.lower()
list = string_lower.split()

count_a = list.count('a')
count_an = list.count('an')
count_the = list.count('the')
count = count_a + count_an + count_the

print('Общее количество артиклей:', count)

# 11.6.4
n = int(input()[1:])

for i in range(n):
    code_string = input().split('#')
    code_string = code_string[0].rstrip()
    print(code_string)

# 11.6.5
string = input()
numbers_str = string.split()
numbers_list = []

for element in numbers_str:
    element = int(element)
    numbers_list.append(element)

numbers_list.sort()
print(*numbers_list, sep=' ')

numbers_list.sort(reverse=True)
print(*numbers_list, sep=' ')

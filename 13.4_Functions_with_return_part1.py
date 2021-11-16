# 13.4
# 13.4.1
# объявление функции
def convert_to_miles(km):
    miles = km * 0.6214
    return miles


# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))


# 13.4.2
# решение 1
# объявление функции
def get_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        return 28


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))


# решение 2
# объявление функции
def get_days(month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[month - 1]


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))


# решение 3
# объявление функции
def get_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 28


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))


# 13.4.3
# объявление функции
def get_factors(num):
    result_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            result_list.append(i)
    return result_list


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))


# 13.4.4
# объявление функции
def number_of_factors(num):
    result_amount = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result_amount = result_amount + 1
    return result_amount


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))


# 13.4.5
# объявление функции
def find_all(target, symbol):
    result_list = []
    for i in range(len(target)):
        if target[i] == symbol:
            result_list.append(i)
    return result_list


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))


# 13.4.6
# объявление функции
def merge(list1, list2):
    result_list = list(list1 + list2)
    result_list.sort()
    return result_list


# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))

# 13.4.7
n = int(input())

list = []
for i in range(n):
    numbers = [int(c) for c in input().split()]
    list = list + numbers
list.sort()

result_list = []
for i in list:
    result_list.append(str(i))

print(' '.join(result_list))

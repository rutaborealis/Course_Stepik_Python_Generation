# 9.1
# 9.1.1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])

# 9.1.2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[39])

# 9.1.3
s = 'abcdefghijklmnop'
len_s = len(s)
for index in range(0, len_s, 2):
    print(s[index])

# 9.1.4
s = 'abc'
len_s = len(s)
for index in range(-1, -len_s - 1, -1):
    print(s[index])

# 9.1.5
name = input()
surname = input()
patronymic = input()

print(surname[0] + name[0] + patronymic[0])

# 9.1.6
string = input()
sum_digit = 0

for char in string:
    digit = int(char)
    sum_digit = sum_digit + digit

print(sum_digit)

# 9.1.7
string = input()
flag = False

for char in string:
    if char in '0123456789':
        flag = True
        break

if flag:
    print('Цифра')
else:
    print('Цифр нет')

# 9.1.8
string = input()
count_star = 0
count_plus = 0

for char in string:
    if char == '*':
        count_star += 1
    if char == '+':
        count_plus += 1

print('Символ + встречается', count_plus, 'раз')
print('Символ * встречается', count_star, 'раз')

# 9.1.9
string = input()
len_string = len(string)
count = 0

for index in range(len_string - 1):
    if string[index] == string[index + 1]:
        count += 1

print(count)

# 9.1.10
string = input()
string = string.lower()
vowels = 'ауоыиэяюёе'
consonants = 'бвгджзйклмнпрстфхцчшщ'
count_vowels = 0
count_consonants = 0

for char in string:
    if char in vowels:
        count_vowels += 1
    if char in consonants:
        count_consonants += 1

print('Количество гласных букв равно', count_vowels)
print('Количество согласных букв равно', count_consonants)

# 9.1.11
n = int(input())
binary = ''

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print(binary)

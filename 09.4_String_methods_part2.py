# 9.4
# 9.4.1
string = input()
count = string.count(' ') + 1
print(count)

# 9.4.2
string = input()
string = string.lower()
print('Аденин:', string.count('а'))
print('Гуанин:', string.count('г'))
print('Цитозин:', string.count('ц'))
print('Тимин:', string.count('т'))

# 9.4.3
n = int(input())
count = 0
count_11_in_string = 0

for i in range(n):
    string = input()
    count_11_in_string = string.count('11')
    if count_11_in_string >= 3:
        count += 1

print(count)

# 9.4.4
string = input()
digits = '0123456789'
count = 0

for char in string:
    if char in digits:
        count += 1

print(count)

# 9.4.5
string = input()

if string.endswith('.com') or string.endswith('.ru'):
    print('YES')
else:
    print('NO')

# 9.4.6
string = input()
count = 0
char_count = ''

for char in string:
    if string.count(char) >= count:
        count = string.count(char)
        char_count = char

print(char_count)

# 9.4.7
string = input()

if string.count('f') == 1:
    print(string.find('f'))
elif string.count('f') >= 2:
    print(string.find('f'), string.rfind('f'))
else:
    print('NO')

# 9.4.8
string = input()
first_index = string.find('h')
last_index = string.rfind('h')
string_copy = string[first_index:last_index + 1]
print(string.replace(string_copy, ''))

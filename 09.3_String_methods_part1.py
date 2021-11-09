# 9.3
# 9.3.1
string_original = input()
string_title = string_original.title()

if string_original == string_title:
    print('YES')
else:
    print('NO')

# 9.3.2
string = input()
string_swapcase = string.swapcase()
print(string_swapcase)

# 9.3.3
string = input()
string_lower = string.lower()
good = 'хорош'

if good in string_lower:
    print('YES')
else:
    print('NO')

# 9.3.4
# решение 1
string = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 0

for char in string:
    if char in alphabet:
        count += 1

print(count)

# решение 2
string, counter = input(), 0
for char in string:
    if char != char.upper():  # условие выполняется только для букв в нижнем регистре
        counter += 1
print(counter)

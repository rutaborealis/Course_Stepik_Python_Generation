# 12 Test
# 12.1
n = int(input())
numbers = list(range(2, n + 1, 2))
print(numbers)

# 12.2
L = input().split(' ')
M = input().split(' ')
result = []

for i in range(len(L)):
    result.append(int(L[i]) + int(M[i]))

print(*result, end=' ')

# 12.3
digits = input().split(' ')
digits_2 = []
sum = 0

for digit in digits:
    sum = sum + int(digit)
    digits_2.append(str(digit))

print('+'.join(digits_2), '=', sum, sep='')

# 12.4
# решение 1
phone_number = input()
phone_num_list = phone_number.split('-')
flag = False

if len(phone_num_list) == 3:
    if (len(phone_num_list[0]) == 3 and phone_num_list[0].isdigit()) and (
            len(phone_num_list[1]) == 3 and phone_num_list[1].isdigit()) and (
            len(phone_num_list[2]) == 4 and phone_num_list[2].isdigit()):
        flag = True
    else:
        flag = False
elif len(phone_num_list) == 4:
    if (int(phone_num_list[0]) == 7 and len(phone_num_list[0]) == 1 and phone_num_list[0].isdigit()) and (
            len(phone_num_list[1]) == 3 and phone_num_list[1].isdigit()) and (
            len(phone_num_list[2]) == 3 and phone_num_list[2].isdigit()) and (
            len(phone_num_list[3]) == 4 and phone_num_list[3].isdigit()):
        flag = True
    else:
        flag = False

if flag:
    print('YES')
else:
    print('NO')

# решение 2
import re

s = input()
pattern = r"7?-?\d{3}-\d{3}-\d{4}"
print('YES' if s in re.findall(pattern, s) else 'NO')

# решение 3
n = input().split("-")
c = [len(i) for i in n]
if c == [3, 3, 4] and ''.join(n).isdigit():
    print("YES")
elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
    print("YES")
else:
    print("NO")

# 12.5
# решение 1
str = input()
str = str.split(' ')
maximum = 0

for item in str:
    if len(item) > maximum:
        maximum = len(item)

print(maximum)

# решение 1
print(max([len(a) for a in input().split()]))

# 12.6
# решение 1
str = input()
str = str.split(' ')
new_str = []

for word in str:
    first_letter = word[0]
    new_word = word[1:] + first_letter + 'ки'
    new_str.append(new_word)

print(*new_str, end=' ')

# решение 2
print(*[a[1:] + a[0] + 'ки' for a in input().split()])

# решение 3
str_ = input().split(' ')
for word in str_:
    word = word + word[0] + 'ки'
    print(word[1:], end=' ')

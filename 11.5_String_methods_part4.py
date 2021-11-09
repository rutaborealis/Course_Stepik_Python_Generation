# 11.5
# 11.5.1
string = input()
list = string.split()
print(*list, sep='\n')

# 11.5.2
string = input()
full_name_list = string.split()
short_name_list = []

for element in full_name_list:
    short_name_list.append(element[0])

short_name_string = '.'.join(short_name_list)

print(short_name_string + '.')

# 11.5.3
string = input()
full_path = string.split('\\')
print(*full_path, sep='\n')

# 11.5.4
string = input()
numbers = string.split()
char = '+'

for element in numbers:
    print(char * int(element))

# 11.5.5
string = input()
ip_list = string.split('.')
flag = True

for element in ip_list:
    element = int(element)
    if element > 255:
        flag = False
        break

if flag:
    print('ДА')
else:
    print('НЕТ')

# 11.5.6
string = input()
separator = input()
sep_string = separator.join(string)
print(sep_string)

# 11.5.7
string = input()
numbers = string.split()
count_pairs = 0

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            count_pairs += 1

print(count_pairs)

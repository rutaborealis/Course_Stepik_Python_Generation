# 10 Test
# 10.1
s = 'Python rocks!'
len_s = len(s)
print(len_s)

# 10.2
s = 'Python rocks!'
char_four = s[3]
print(char_four)

# 10.3
s = 'Python rocks!'
string = s[1:5]
print(string)

# 10.4
s = '    Python rocks!     '
print(s.strip())

# 10.5
s = 'Python rocks!'
print(s.upper())

# 10.6
s = 'Python rocks!'
print(s.replace('o', '@'))

# 10.7
string = input()

for index in range(len(string)):
    if index % 3 != 0:
        print(string[index], end='')

# 10.8
string = input()
print(string.replace('1', 'one'))

# 10.9
string = input()
print(string.replace('@', ''))

# 10.10
# решение 1
string = input()
index = 0
count = 0

for i in range(len(string)):
    if string[i] == 'f' and count < 2:
        index = i
        count += 1

if count == 2:
    print(index)
elif count == 1:
    print(-1)
elif count == 0:
    print(-2)

# решение 2
string = input()
if string.count('f') == 1:
    print('-1')
elif string.count('f') == 0:
    print(-2)
elif string.count('f') > 1:
    string = string.replace('f', '+', 1)
    print(string.find('f'))

# 10.11
string = input()
h_first = string.find('h')
h_last = string.rfind('h')
slice = string[h_first + 1:h_last]
slice = slice[::-1]

print(string[:h_first] + slice + string[h_last:])

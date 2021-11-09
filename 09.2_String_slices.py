# 9.2
# 9.2.1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:13])

# 9.2.2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[40:])

# 9.2.3
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

# 9.2.4
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

# 9.2.5
string = input()
reverse_string = string[::-1]

if string == reverse_string:
    print('YES')
else:
    print('NO')

# 9.2.6
string = input()

print(len(string))
print(string * 3)
print(string[0])
print(string[:3])
print(string[-3:])
print(string[::-1])
print(string[1:-1])

# 9.2.7
string = input()

print(string[2])
print(string[-2])
print(string[:5])
print(string[:-2])
print(string[::2])
print(string[1::2])
print(string[::-1])
print(string[-1::-2])

# 9.2.8
string = input()
len_string = len(string)

if len_string % 2 == 0:
    middle_string = len_string // 2
    string_1 = string[:middle_string]
    string_2 = string[middle_string:]
else:
    middle_string = len_string // 2 + 1
    string_1 = string[:middle_string]
    string_2 = string[middle_string:]

print(string_2 + string_1)

# 11.7
# 11.7.1
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m[1::] for m in keywords]
print(new_keywords)

# 11.7.2
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(m) for m in keywords]
print(lengths)

# 11.7.3
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m for m in keywords if len(m) >= 5]
print(new_keywords)

# 11.7.4
palindromes = [i for i in range(100, 1000) if (i % 10 == i // 100)]
print(palindromes)

# 11.7.5
n = int(input())
numbers = [print(i ** 2) for i in range(1, n + 1)]

# 11.7.6
str = input()
str = str.split(' ')
numbers = [print(int(str[i]) ** 3, end=' ') for i in range(len(str))]

# 11.7.7
str = input()
str = str.split(' ')
words = [print(word) for word in str]

# 11.7.8
str = input()
digits = [print(char, end='') for char in str if char.isdigit()]

# 11.7.9
# решение 1
str = input()
digits = str.split(' ')
numbers = []

for digit in digits:
    digit = int(digit)
    numbers.append(digit)

for number in numbers:
    if (number % 2 == 0 and (number ** 2) % 10 != 4):
        print(number ** 2, end=' ')

# решение 2
print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])

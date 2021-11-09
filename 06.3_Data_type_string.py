# 6.3
# 6.3.1
a = '"Python is a great language!", said Fred.'
b = '''"I don't ever remember having this much fun before."'''
c = a + ' ' + b
print(c)

# 6.3.2
firstname = input()
lastname = input()
lastname = lastname + '!'
print('Hello', firstname, lastname, 'You just delved into Python')

# 6.3.3
team = input()
n = len(str(team))
print('Футбольная команда', team, 'имеет длину', n, 'символов')

# 6.3.4
city1 = input()
city2 = input()
city3 = input()

len_city1 = len(city1)
len_city2 = len(city2)
len_city3 = len(city3)

maximum = max(len_city1, len_city2, len_city3)
minimum = min(len_city1, len_city2, len_city3)

if minimum == len_city1:
    result_min = city1
elif minimum == len_city2:
    result_min = city2
elif minimum == len_city3:
    result_min = city3

if maximum == len_city1:
    result_max = city1
elif maximum == len_city2:
    result_max = city2
elif maximum == len_city3:
    result_max = city3

print(result_min)
print(result_max)

# 6.3.5
a = len(input())
b = len(input())
c = len(input())

maximum = max(a, b, c)
minimum = min(a, b, c)
middle = (a + b + c) - (maximum + minimum)

d1 = middle - minimum
d2 = maximum - middle

if d1 == d2:
    print('YES')
else:
    print('NO')

# 6.3.6
a = input()
b = 'синий'

if b in a:
    print('YES')
else:
    print('NO')

# 6.3.7
a = input()
b = 'суббота'
c = 'воскресенье'

if (b in a) or (c in a):
    print('YES')
else:
    print('NO')

# 6.3.8
email = input()
email_at = '@'
email_dot = '.'

if (email_at in email) and (email_dot in email):
    print('YES')
else:
    print('NO')

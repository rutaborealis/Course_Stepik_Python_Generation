# 6.2
from math import *

# 6.2.1
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

a1 = (x1 - x2) ** 2
a2 = (y1 - y2) ** 2
a3 = a1 + a2
p = sqrt(a3)

print(p)

# 6.2.2
from math import *

r = float(input())
s = pi * r ** 2
c = 2 * pi * r

print(s)
print(c)

# 6.2.3
from math import *

a = float(input())
b = float(input())

average = (a + b) / 2
geometric_mean = sqrt(a * b)
harmonic_mean = (2 * a * b) / (a + b)
mean_square = sqrt((a ** 2 + b ** 2) / 2)

print(average)
print(geometric_mean)
print(harmonic_mean)
print(mean_square)

# 6.2.4
from math import *

x = float(input())
r = (x * pi) / 180

result = sin(r) + cos(r) + (tan(r) ** 2)

print(result)

# 6.2.5
from math import *

x = float(input())

a = ceil(x)
b = floor(x)
result = a + b

print(result)

# 6.2.6
from math import *

a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - (4 * a * c)

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif d == 0:
    x = -b / (2 * a)
    if x == 0:
        print('0.0')
    else:
        print(x)
else:
    print('Нет корней')

# 6.2.6
from math import *

n = float(input())
a = float(input())

action1 = n * a ** 2
x = (pi / n)
action2 = 4 * tan(x)
s = action1 / action2

print(s)

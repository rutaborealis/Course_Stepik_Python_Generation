# 7.5.1
# 7.5.1
n = int(input())

while n != 0:
    last_digit = n % 10
    print(last_digit)
    n = n // 10

# 7.5.2
n = int(input())

while n != 0:
    last_digit = n % 10
    print(last_digit, end='')
    n = n // 10

# 7.5.3
n = int(input())
last_digit = n % 10
maximum = last_digit
minimum = last_digit

while n != 0:
    if last_digit > maximum:
        maximum = last_digit
    elif last_digit < minimum:
        minimum = last_digit
    n = n // 10
    last_digit = n % 10

print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)

# 7.5.4
n = int(input())
last_digit = n % 10
sum_digits = 0
counter_digits = 0
mult_digits = 1

while n != 0:
    current_last_digit = n % 10
    sum_digits = sum_digits + current_last_digit
    counter_digits = counter_digits + 1
    mult_digits = mult_digits * current_last_digit
    n = n // 10

if n == 0:
    first_digit = current_last_digit

average_digits = sum_digits / counter_digits

sum_first_last = first_digit + last_digit

print(sum_digits)
print(counter_digits)
print(mult_digits)
print(average_digits)
print(first_digit)
print(sum_first_last)

# 7.5.5
n_original = int(input())
n = n_original
last_digit = n_original % 10

while n != 0:
    pre_last_digit = last_digit
    last_digit = n % 10
    n = n // 10

if last_digit == n_original:
    pre_last_digit = n_original

print(pre_last_digit)

# 7.5.6
n = int(input())
last_digit = n % 10
flag = True

while n != 0:
    pre_last_digit = last_digit
    last_digit = n % 10
    if pre_last_digit == last_digit:
        flag = True
    else:
        flag = False
        n = 0
    n = n // 10

if flag:
    print('YES')
else:
    print('NO')

# 7.5.7
n = int(input())
last_digit = n % 10
flag = True

while n != 0:
    pre_last_digit = last_digit
    last_digit = n % 10
    if pre_last_digit <= last_digit:
        flag = True
    else:
        flag = False
        n = 0
    n = n // 10

if flag:
    print('YES')
else:
    print('NO')

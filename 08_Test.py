# 8 Test
# 8.4
n = int(input())
string1 = ('*' + ' ' * 17 + '*')
string2 = ('*' * 19)

for i in range(1, n + 1):
    if (i == 1) or (i == n):
        print(string2)
    else:
        print(string1)

# 8.5
n = int(input())

while n > 1000:
    n = n // 10

last_digit = n % 10

print(last_digit)

# 8.6
n = int(input())
last_digit = n % 10

count3 = 0
count_last_digit = 0
count_even = 0
sum_5 = 0
mult_7 = 1
count_0_5 = 0

while n != 0:
    current_last_digit = n % 10
    if current_last_digit == 3:
        count3 = count3 + 1
    if current_last_digit == last_digit:
        count_last_digit = count_last_digit + 1
    if current_last_digit % 2 == 0:
        count_even = count_even + 1
    if current_last_digit > 5:
        sum_5 = sum_5 + current_last_digit
    if current_last_digit > 7:
        mult_7 = mult_7 * current_last_digit
    if (current_last_digit == 0) or (current_last_digit == 5):
        count_0_5 = count_0_5 + 1
    n = n // 10

print(count3)
print(count_last_digit)
print(count_even)
print(sum_5)
print(mult_7)
print(count_0_5)

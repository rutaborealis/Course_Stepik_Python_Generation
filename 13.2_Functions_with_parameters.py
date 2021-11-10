# 13.2
# 13.2.1
def draw_triangle(fill, base):
    mid = base // 2 + 1
    for i in range(1, base + 1):
        if i <= mid:
            print(fill * i)
        else:
            print(fill * (base - i + 1))


fill = input()
base = int(input())

draw_triangle(fill, base)


# 13.2.2
def print_fio(name, surname, patronymic):
    name = name[0]
    surname = surname[0]
    patronymic = patronymic[0]
    print(surname.upper() + name.upper() + patronymic.upper())


name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)


# 13.2.3
def print_digit_sum(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    print(sum)


n = int(input())

print_digit_sum(n)

# 13.5
# 13.5.1
# объявление функции
def is_valid_triangle(a, b, c):
    if (a < b + c) and (b < a + c) and (c < a + b):
        return True
    else:
        return False


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))


# 13.5.2
# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))


# 13.5.3
# объявление функции
def get_next_prime(num):
    n = num + 1
    while True:  # Есть граница, выше которой не надо
        # Запускаем перебор для проверки на делимость
        for i in range(2, n):  # От единицы до нашего числа включительно!
            if n % i == 0:  # Если нет остатка, то есть, число делится на что-то
                n += 1  # Добавляем единицу
                break  # Прерываем цикл
        else:  # Дошли до конца цикла
            return n  # Значит, наше число простое


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))


# 13.5.4
# объявление функции
def is_password_good(password):
    a = (len(password) > 7)
    b = (password != password.lower())
    c = (password != password.upper())
    d = not password.isalpha()
    return a and b and c and d


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))


# 13.5.5
# объявление функции
def is_one_away(word1, word2):
    count = 0
    flag1 = False
    flag2 = False
    if len(word1) == len(word2):
        flag1 = True
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count = count + 1
    if count == 1:
        flag2 = True
    return flag1 and flag2


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))


# 13.5.6
# объявление функции
def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))


# 13.5.7
# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]


def is_valid_password(password):
    password_list = password.split(':')
    if len(password_list) == 3:
        flag1 = is_palindrome(password_list[0])
        flag2 = is_prime(int(password_list[1]))
        flag3 = False
        if int(password_list[2]) % 2 == 0:
            flag3 = True
        return flag1 and flag2 and flag3
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))


# 13.5.8
# объявление функции
def is_correct_bracket(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')
    # Возвращаем True, если text с пустой строкой
    return not text


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))


# 13.5.9
# объявление функции
def convert_to_python_case(text):
    python_list = []
    for c in text:
        if c == c.lower() or c.isdigit():
            python_list.append(c)
        else:
            python_list.append('_')
            python_list.append(c.lower())
    return ''.join(python_list[1:])


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

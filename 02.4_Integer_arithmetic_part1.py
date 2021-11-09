# 2.4
# 2.4.1
print('Введите целое число:')
num_1 = int(input())
num_2 = num_1 + 1
num_3 = num_2 + 1

print()
print('Полученная последовательность:')

print(num_1)
print(num_2)
print(num_3)
print()

# 2.4.2
print('Введите 3 целых числа:')
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print('Сумма введенных чичел:')
total = num_1 + num_2 + num_3
print(total)
print()

# 2.4.3
print('Введите длину ребра куба:')
cube_lenght = int(input())
V_cube = cube_lenght ** 3
S_cube = 6 * cube_lenght ** 2

print('Вычисленные значения:')
print('Объем куба =', V_cube)
print('Площадь полной поверхности куба =', S_cube)
print()

# 2.4.4
print('Введите значения функции:')
a = int(input())
b = int(input())

# f(a,b) = 3(a+b)^3+275b^2-127a-41
f = 3 * ((a + b) ** 3) + 275 * (b ** 2) - 127 * a - 41
print('Значение функции с введенными параметрами:', f)
print()

# 2.4.5
print('Введите целое число:')
num = int(input())
num_next = num + 1
num_prev = num - 1

print('Следующее за числом', num, 'число:', num_next)
print('Для числа', num, 'предыдущее число:', num_prev)
print()

# 2.4.6
print('Введите стоимость монитора:')
cost_monitor = int(input())
print('Введите стоимость системного блока:')
cost_system = int(input())
print('Введите стоимость клавиатуры:')
cost_keyboard = int(input())
print('Введите стоимость мыши:')
cost_mouse = int(input())

cost_total = cost_monitor + cost_system + cost_keyboard + cost_mouse
total = 3 * cost_total

print('Стоимость для 3(!) компьютеров:')
print(total)
print()

# 2.4.7
print('Введите 2 целых числа:')
a = int(input())
b = int(input())

sum_a_b = a + b
dif_a_b = a - b
prod_a_b = a * b

print(a, '+', b, '=', sum_a_b)
print(a, '-', b, '=', dif_a_b)
print(a, '*', b, '=', prod_a_b)
print()

# 2.4.8
print('Введите параметры арифметической прогрессии')
print('Введите первый член арифметической прогрессии:')
a1 = int(input())
print('Введите разность арифметической прогрессии:')
d = int(input())
print('Введите количество членов арифметической прогрессии:')
n = int(input())

progression_n = a1 + d * (n - 1)

print('N-й член арифметической прогрессии:', progression_n)
print()

# 2.4.9
print('Введите целое положительное число x:')
x1 = int(input())
x2 = 2 * x1
x3 = 3 * x1
x4 = 4 * x1
x5 = 5 * x1

print('Рассчитанная последовательность:')
print(x1, x2, x3, x4, x5, sep='---')

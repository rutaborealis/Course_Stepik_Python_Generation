# 15.5
# Caesar cipher
# abc = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

text = input().lower()
key = int(input())
code = ''

for char in text:
    if char in abc:
        position = abc.find(char)
        new_position = position + key
        code = code + abc[new_position]
    else:
        code = code + char

print(code)

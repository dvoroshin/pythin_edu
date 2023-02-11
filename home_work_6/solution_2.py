from random import randint

li = [randint(0, 9) for i in range(15)]

print(li)

n_input = input('Введите число: ')

index = 0
count = 0

while index < len(li)-len(n_input):
    temp_str = ''
    for i in range(len(n_input)):
        temp_str += str(li[index+i])
    if temp_str == n_input:
        count += 1
    index += 1

if count > 0:
    print(f'{li} -> Да, {count} раз(а)')
else:
    print(f'{li} -> Нет')

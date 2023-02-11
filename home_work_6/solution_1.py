n_from_input = input('Введите натуральное число N: ')
exp = n_from_input+'+'+n_from_input+n_from_input + \
    '+'+n_from_input+n_from_input+n_from_input
li = list(map(int, exp.split('+')))
result = li[0]+li[1]+li[2]
print(f'Результат преобразования {exp}: {result}')

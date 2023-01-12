number = int(input('Введите число: '))
print(f'N={number} -> ', end='')
for i in range(1, number+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    print(f'{factorial} ', end='')

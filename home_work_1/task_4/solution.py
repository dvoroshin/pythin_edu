num = int(input(
    "Введите целое число для вывода всех четных чисел в диапазоне от 1 до N: "))

if num > 0:
    while num > 1:
        if num % 2 == 0:
            print(f'{num} ')
        num = num-1
else:
    while num < -1:
        if num % 2 == 0:
            print(f'{num} ')
        num = num+1

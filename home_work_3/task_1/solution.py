number = int(input('Введите число: '))
fib_1 = 0
fib_2 = 1
data = open('fib.txt', mode='w', encoding='utf-8')
for i in range(number):
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    data.write(str(fib_1)+'\n')

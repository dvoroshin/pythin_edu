num = int(input('Введите число: '))
numbers = str(list(range(-num, num+1)))

for i in range(1, len(numbers)-1):
    buf = numbers[i]
    numbers[i] = numbers[:i+3]
    numbers[:i+3] = buf

for i in range(1, len(numbers)-1):
    print(numbers[i])

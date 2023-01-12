num = int(input('Введите число: '))
numbers = list(range(-num, num+1))
result = numbers[-2:] + numbers[:-2]
print(result)

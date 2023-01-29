n = int(input('Введите число N: '))

count = 2

list = []

while n != 1:
    if n % count == 0:
        list.append(count)
        n //= count
    else:
        count += 1

print(list)

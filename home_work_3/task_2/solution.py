let = input('Введите букву: ')

data = open('fruits.txt', mode='r', encoding='utf-8')

fruits = data.readline().split()

for _ in fruits:
    if _[0] == let:
        print(_)

data.close()

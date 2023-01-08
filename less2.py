def task1():
    print('x | y | ¬ x V y')
    for x in range(2):
        for y in range(2):
            print(f'{x} | {y} | {int(not x or y)}')


def task2():
    phrase = 'qwe'
    length_phrase = len(phrase)
    text = 'qweqwerqweqwewqewrewq'
    count = 0
    for i in range(len(text) - length_phrase + 1):
        text_part = text[i:i + length_phrase]
        if phrase == text_part:
            count += 1
    print(f'Первая строка содержится во второй {count} раз(-а)')


def task3():
    number = int(input('Введите число: '))
    result = []
    for i in range(number+1):
        result.append((-3)**i)
    print(result)


def task4():
    result = 0
    for i in range(1, 10000):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 10:
            result += 1
    print(result)

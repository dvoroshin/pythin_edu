li = [i for i in range(1, 12)]

for i in range(1, 11):
    temp_li = li
    if i % 2 == 0:
        temp_li = list(filter(lambda x: x % 2 != 0, temp_li))
    if i % 3 == 0:
        temp_li = list(filter(lambda x: x % 3 != 0, temp_li))
    if i % 5 == 0:
        temp_li = list(filter(lambda x: x % 5 != 0, temp_li))
    for j in temp_li:
        if j > i:
            print(f'{i}/{j}')

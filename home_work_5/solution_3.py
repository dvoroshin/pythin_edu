from random import randint

count_el = 6

li = [randint(1, 10) for _ in range(count_el)]

print(li)

count = 0
temp_li = []
flag = 0

for j in range(0, len(li)-1):
    for i in range(j+1, len(li)):
        if li[i] == li[j] and li[i] not in temp_li:
            count += 1
            flag = 1
    if (flag == 1):
        temp_li.append(li[j])
        flag = 0

print(count, list(set(li)))

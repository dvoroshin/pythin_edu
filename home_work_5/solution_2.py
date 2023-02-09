from random import randint

count_el = 50

li = [randint(1, 9) for _ in range(count_el)]
result = []

print(li)

random_index = randint(0, count_el-1)
result.append(li[random_index])
index_result = 0
while random_index < count_el-1:
    temp_index = randint(random_index, count_el-1)
    if temp_index > random_index:
        random_index = temp_index
        if li[random_index] > result[index_result]:
            index_result += 1
            result.append(li[random_index])

print(result)

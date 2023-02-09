from random import randint

print(list(filter(lambda x: x > 5, [randint(1, 10) for _ in range(21)])))

data_1 = open('mch1.txt', mode='r', encoding='utf-8')
data_2 = open('mch2.txt', mode='r', encoding='utf-8')

string_1 = data_1.read().replace(' ', '')
string_2 = data_2.read().replace(' ', '')

data_1.close()
data_2.close()

print(string_1, string_2)

calc = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        }


def count_ch(string):
    count = 0
    for i in string:
        if i == '+' or i == '-':
            count += 1
    return count


i = 0

while i < len(string_1):
    if string_1[i] == 'x' and string_1[i-1] == '+' or string_1[i-1] == '-':
        string_1 = string_1[:i-1] + '1' + string_1[i-1:]
    i += 1

i = 0

while i < len(string_2):
    if string_2[i] == 'x' and string_2[i-1] == '+' or string_2[i-1] == '-':
        string_2 = string_2[:i-1] + '1' + string_2[i-1:]
    i += 1

count_ch1 = count_ch(string_1)
count_ch2 = count_ch(string_2)

print(count_ch1, count_ch2, string_1, string_2)

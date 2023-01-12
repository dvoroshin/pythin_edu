phrase = 'one'
length_phrase = len(phrase)
text = 'onetwonine'
count = 0
for j in range(length_phrase):
    count = 0
    for i in range(len(text)):
        if phrase[j] == text[i]:
            count += 1
    print(f'{phrase[j]} встречается {count} раз(-а)')

phrase_dictionary = \
    {
        'привет': 'здравствуй',
        'как тебя зовут?': 'Ботинок'
    }

start = True

while start:
    phrase = input('Вы: ')
    if phrase in phrase_dictionary.keys():
        print(f'Бот: {phrase_dictionary[phrase]}')
    elif phrase == 'выход':
        start = False
    else:
        print(f'Бот: не понимаю...')

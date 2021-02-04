from mtranslate import translate

try:
    with open('./sample.txt', mode='r', encoding='utf8') as sample:
        with open('translated-google.txt', mode='w', encoding='utf8') as translated:
            translated.write(translate(sample.read(), 'si'))
except FileNotFoundError as err:
    print(f'File not found: {err}')
except IOError as err:
    print(f'IO error: {err}')

from mtranslate import translate


def translate_and_write(text, lang):
    with open(f'{lang}.txt', mode='w', encoding='utf8') as translated:
        translated.write(translate(text, lang))


try:
    with open('./sample.txt', mode='r', encoding='utf8') as sample:
        sample_text = sample.read()
except FileNotFoundError as err:
    print(f'File not found: {err}')
except IOError as err:
    print(f'IO error: {err}')

translate_and_write(sample_text, 'si')
translate_and_write(sample_text, 'ta')
translate_and_write(sample_text, 'es')
translate_and_write(sample_text, 'ru')
translate_and_write(sample_text, 'ja')

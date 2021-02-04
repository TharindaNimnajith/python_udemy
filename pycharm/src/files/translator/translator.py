from translate import Translator

try:
    with open('./sample.txt', mode='r') as sample:
        translator = Translator(to_lang='es')
        with open('./translated.txt', mode='w') as translated:
            translated.write(translator.translate(sample.read()))
except FileNotFoundError as err:
    print(f'File not found: {err}')
except IOError as err:
    print(f'IO error: {err}')

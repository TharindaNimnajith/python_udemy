import pyjokes

print(pyjokes.get_joke('en', 'neutral'))

jokes = pyjokes.get_jokes()

for joke in jokes:
    print(joke)


# pip3 install pyjokes
# pip3 list
# pip3 uninstall pyjokes
# pip3 install pyjokes==0.4.0
# pip3 list

# pip install pyjokes
# pip list
# pip uninstall pyjokes
# pip install pyjokes==0.4.0
# pip list

# py jokes.py
# python jokes.py

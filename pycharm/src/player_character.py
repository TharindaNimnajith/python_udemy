class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age


PlayerCharacter.__init__(player := PlayerCharacter('Temp', 90), 'Nuvindu', 20)
print(player.name)
print(player.age)

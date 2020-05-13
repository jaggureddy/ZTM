class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return self

    def speak(self):
        print('run')


player1 = Player('Jaggu', 20)

print(player1.run())
player1.speak = 'Boo'
print(player1.speak)

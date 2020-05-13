class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attack with arrows {self.arrows}')


wiz = Wizard('Jaggu', 30, 'test@email.com')
arc = Archer('Jag', 100, 'arc@gmail.com')

wiz.attack()
wiz.sign_in()
print(wiz.email)
arc.attack()
arc.sign_in()
print(arc.email)

class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))


class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack_arrows(self):
        print(f'attack with arrows {self.arrows}')


wiz = Wizard('Jaggu', 30)
arc = Archer('Jag', 100)


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hybrid = Hybrid('J', 30, 50)
hybrid.sign_in()
hybrid.attack()
hybrid.attack_arrows()

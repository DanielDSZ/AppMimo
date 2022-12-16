class Player:
    def __int__(self, name):
        self.name = name

class Computer(Player):
    def __int__(self):
        super().__int__('NPC')

    def respond(self, player):
        print('Hello', player.name, 'I am', self.name)

class User(Player):
    def __int__(self, name, level):
        super().__int__(name)
        self.level = level

    def greet(self):
        print('Hi! What is your name?')

computer = Computer()
user = User('User', 1)
user.greet()
computer.respond(user)

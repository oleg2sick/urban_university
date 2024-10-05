class Horse:
    def __init__(self, *args):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__(*args)

    def run(self, dx):
        if not isinstance(dx, int):
            raise ArithmeticError(f'{dx} не принадлежит к типу int' )
        self.x_distance += dx

class Eagle:
    def __init__(self, *args):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        super().__init__(*args)

    def fly(self, dy):
        if not isinstance(dy, int):
            raise ArithmeticError(f'{dy} не принадлежит к типу int' )
        self.y_distance += dy

class Pegasus(Horse, Eagle):

    def __init__(self, *args):
        super().__init__(*args)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

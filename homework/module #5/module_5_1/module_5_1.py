class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, go_to):
        if go_to > self.number_of_floors or go_to < 1:
            print('Такого этажа не существует')
        else:
            floor_go_to = [i for i in range(1, go_to + 1)]
            print(*floor_go_to, sep = '\n')
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
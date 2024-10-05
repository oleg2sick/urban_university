import math

class Figure:
    sides_count = 0
    def __init__(self, sides, color):
        self.__sides = sides
        self.__color = color
        self.filled = False

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 < r < 255 and 0 < g < 255 and 0 < b < 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b
        return

    def __is_valid_sides(self, *args):
        for arg in args:
            if len(args) == self.sides_count and isinstance(arg, int) and arg > 0:
                return True
            elif len(args) != self.sides_count and isinstance(arg, int) and arg > 0:
                list2 = []
                for j in range(self.sides_count):
                    list2.append(1)
            else:
                return False


    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        side = 0
        for i in self.__sides:
            side += i
        return side

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(sides, color)
        self.__sides = sides
        self.__radius = round(self.__sides / (2 * math.pi), 2)

    def get_square(self):
        return round(math.pi * math.pow((self.__radius), 2))


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(sides, color)

    def get_square(self, a, b, c):
        half = len(self) / 2
        return round(math.sqrt(half * (half - a) * (half - b) * (half - c)), 2)

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__([sides] * 12, color)
        self.__sides = sides

    def get_volume(self):
        return int(math.pow(self.get_sides()[0], 3))

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

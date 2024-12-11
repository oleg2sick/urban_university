import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):

    is_frozen = True


    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_runner = Runner('Leonid', -1)
            for dist in range(10):
                test_runner.walk()
            self.assertEqual(test_run.distance, self.speed * 10)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning(msg='Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_runner = Runner(123, 5)
            for dist in range(10):
                test_runner.run()
            self.assertEqual(test_run.distance, self.speed * 10)
        except TypeError:
            logging.warning(msg='Неверный тип данных для объекта Runner', exc_info=True)

if __name__ == '__main__':
    unittest.main()

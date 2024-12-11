import sys
sys.path.append('./HumanMoveTest')

import unittest
import runner
import runner_and_tournament as rat

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_run = runner.Runner('any')
        for dist in range(10):
            test_run.walk()
        self.assertEqual(test_run.distance, 50)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_run = runner.Runner('any')
        for dist in range(10):
            test_run.run()
        self.assertEqual(test_run.distance, 100)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        first_runner = runner.Runner('first')
        second_runner = runner.Runner('second')
        for dist in range(10):
            first_runner.walk()
            second_runner.run()
        self.assertNotEqual(first_runner.distance, second_runner.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = []

    def setUp(self):
        global first_runner, second_runner, third_runner
        first_runner = rat.Runner('Усэйн', 10)
        second_runner = rat.Runner('Андрей', 9)
        third_runner = rat.Runner('Ник', 3)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_first_third(self):
        first_tour = rat.Tournament(90, first_runner, third_runner)
        result = first_tour.start()
        all_results.append(result)
        last_one = result[max(result.keys())]
        self.assertTrue(last_one, 'Ник')

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_second_third(self):
        second_tour = rat.Tournament(90, second_runner, third_runner)
        result = second_tour.start()
        all_results.append(result)
        last_one = result[max(result.keys())]
        self.assertTrue(last_one, 'Ник')

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_all(self):
        third_tour = rat.Tournament(90, first_runner, second_runner, third_runner)
        result = third_tour.start()
        all_results.append(result)
        last_one = result[max(result.keys())]
        self.assertTrue(last_one, 'Ник')

    @classmethod
    def tearDownClass(cls):
        for res in all_results:
            print(res)

if __name__ == '__main__':
    unittest.main()


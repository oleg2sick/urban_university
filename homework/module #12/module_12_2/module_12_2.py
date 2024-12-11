import sys

sys.path.append('./HumanMoveTests')

import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = []

    def setUp(self):
        global first_runner, second_runner, third_runner
        first_runner = rat.Runner('Усэйн', 10)
        second_runner = rat.Runner('Андрей', 9)
        third_runner = rat.Runner('Ник', 3)

    def test_first_third(self):
        first_tour = rat.Tournament(90, first_runner, third_runner)
        result = first_tour.start()
        all_results.append(result)
        last_one = result[max(result.keys())]
        self.assertTrue(last_one, 'Ник')

    def test_second_third(self):
        second_tour = rat.Tournament(90, second_runner, third_runner)
        result = second_tour.start()
        all_results.append(result)
        last_one = result[max(result.keys())]
        self.assertTrue(last_one, 'Ник')

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


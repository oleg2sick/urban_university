import sys

sys.path.append('./HumanMoveTest')

import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.first_runner = rat.Runner('Усэйн', 10)
        self.second_runner = rat.Runner('Андрей', 9)
        self.third_runner = rat.Runner('Ник', 3)

    def test_first_third(self):
        first_tour = rat.Tournament(90, self.first_runner, self.third_runner)
        result = first_tour.start()
        TournamentTest.all_results.append(result)
        last_one = result[max(result.keys())]
        self.assertTrue(last_one, 'Ник')

    def test_second_third(self):
        second_tour = rat.Tournament(90, self.second_runner, self.third_runner)
        result = second_tour.start()
        TournamentTest.all_results.append(result)
        last_one = result[max(result.keys())]
        self.assertTrue(last_one, 'Ник')

    def test_all(self):
        third_tour = rat.Tournament(90, self.first_runner, self.second_runner, self.third_runner)
        result = third_tour.start()
        TournamentTest.all_results.append(result)
        last_one = result[max(result.keys())]
        self.assertTrue(last_one, 'Ник')

    @classmethod
    def tearDownClass(cls):
        for res in TournamentTest.all_results:
            print(res)

if __name__ == '__main__':
    unittest.main()


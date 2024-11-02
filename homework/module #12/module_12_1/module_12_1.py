import sys
sys.path.append('./HumanMoveTest')

import unittest
import runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_run = runner.Runner('any')
        for dist in range(10):
            test_run.walk()
        self.assertEqual(test_run.distance, 50)

    def test_run(self):
        test_run = runner.Runner('any')
        for dist in range(10):
            test_run.run()
        self.assertEqual(test_run.distance, 100)

    def test_challenge(self):
        first_runner = runner.Runner('first')
        second_runner = runner.Runner('second')
        for dist in range(10):
            first_runner.walk()
            second_runner.run()
        self.assertNotEqual(first_runner.distance, second_runner.distance)


if __name__ == '__main__':
    unittest.main()

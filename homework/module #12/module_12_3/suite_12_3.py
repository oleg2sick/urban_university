import sys
sys.path.append('./HumanMoveTest')

import unittest
import tests_12_3


tester = unittest.TestSuite()
tester.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tester.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

test_object = unittest.TextTestRunner(verbosity = 2)
test_object.run(tester)

import unittest
import problem2
class Test(unittest.TestCase):
    def test(self):
        result = problem2.nonfactors_calculate(15)
        self.assertEqual(result, 9)
if __name__ == '__main__':
	unittest.main()
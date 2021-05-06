import unittest
import problem1B
class Test(unittest.TestCase):
    def test(self):
        result = problem1B.reverse_each_word("flipped class room is important")
        self.assertEqual(result, "deppilf ssalc moor si tnatropmi")
if __name__ == '__main__':
	unittest.main()
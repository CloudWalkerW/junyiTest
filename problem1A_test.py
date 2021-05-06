import unittest
import problem1A
class Test(unittest.TestCase):
    def test(self):
        result = problem1A.reverse("junyiacademy")
        self.assertEqual(result, "ymedacaiynuj")
if __name__ == '__main__':
	unittest.main()
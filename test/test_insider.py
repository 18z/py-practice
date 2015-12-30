import unittest
from insider import insider

class TestInsiderFunction(unittest.TestCase):

    def test_volume(self):
        host = insider("redbull")
        self.assertEqual("volume is enough use", host.check_volume())

if __name__ == '__main__':
    unittest.main()

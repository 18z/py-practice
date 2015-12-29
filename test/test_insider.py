import unittest
from insider import insider

class TestInsiderFunction(unittest.TestCase):

    # def test_ping(self):
    #     host = insider("redbull")
    #     self.assertEqual("8.8.8.8 is Up", host.check_ip("8.8.8.8"))
    #
    # def test_firewall_log(self):
    #     host = insider("redbull")
    #     self.assertEqual("no logs yet", host.check_firewall_log())

    def test_volume(self):
        host = insider("redbull")
        self.assertEqual("volume is enough use", host.check_volume())

if __name__ == '__main__':
    unittest.main()

import unittest

from consolas import Console

class ConsoleTest(unittest.TestCase):
    def test_console_equalty(self):
        c1 = Console(1, None, None)
        c2 = Console(1,None,"asdf")
        self.assertEqual( c1, c2 )

unittest.main()
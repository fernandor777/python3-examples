from unittest import TestCase
import lifebeing
import datetime

class HumanTest(TestCase):
    def setUp(self):
        self.human = lifebeing.Human("Fer", 36)
        
    def test_birthage(self):
        ba = datetime.datetime.now().year - 36
        human = lifebeing.Human("Fer", 36)
        self.assertEqual(ba,human.birthyear)
    


import unittest

from translator import french_to_english, english_to_french

class TestfrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(None, french_to_english(None))
        self.assertEqual(None, english_to_french(None))
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
unittest.main()        
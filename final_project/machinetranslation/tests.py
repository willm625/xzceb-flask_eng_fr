import unittest

from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test1(self):
        print('frenchToEgnlish - assertEqual')
        self.assertEqual(None, french_to_english(None))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test2(self):
        print('frenchToEnglish - assertNotEqual')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bye')
        self.assertNotEqual(french_to_english(None), 'Hello')
        
    def test3(self):
        print('englishToFrench - assertEqual')
        self.assertEqual(None, english_to_french(None))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
    def test4(self):
        print('englishToFrench - assertNotEqual')
        self.assertNotEqual(english_to_french('Hello'), 'Goodbye')
        self.assertNotEqual(english_to_french(None), 'Hello')
        
unittest.main()        
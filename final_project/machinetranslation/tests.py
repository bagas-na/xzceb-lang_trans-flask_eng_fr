"Unit tests for translator.py"
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    "Test case class for translating english to french"
    def test1(self):
        "Test case for translating english to french"
        self.assertEqual(english_to_french("lunch"), "Déjeuner")
        self.assertEqual(english_to_french("shy"), "Timide")
        self.assertEqual(english_to_french("cheese"), "Fromage")
        self.assertEqual(english_to_french("potato"), "Pomme de terre")
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    "Test case class for translating french to english"
    def test1(self):
        "Test case for translating french to english"
        self.assertEqual(french_to_english("ananas"), "Pineapple")
        self.assertEqual(french_to_english("étude"), "Study")
        self.assertEqual(french_to_english(""), "Room")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()

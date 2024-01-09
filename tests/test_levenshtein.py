from unittest import TestCase
from Levenshtein import distance


class TestLevenshtein(TestCase):
    def test_levenshtein(self):
        self.assertEqual(distance("foo", "nooo"), 2)

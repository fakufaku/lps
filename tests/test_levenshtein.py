from unittest import TestCase
from Levenshtein import distance
from lps.lps import LevenshteinPhonemeSimilarity
import soundfile as sf


class TestLevenshtein(TestCase):
    def test_levenshtein(self):
        self.assertEqual(distance("foo", "nooo"), 2)

    def test_levenshtein_sim(self):
        (ref, _), (sample, _) = sf.read("tests/resources/speech.wav"), sf.read("tests/resources/speech_bab_0dB.wav")
        lps = LevenshteinPhonemeSimilarity()
        self.assertEqual(lps(ref, ref), 1.0)
        self.assertLess(lps(sample, ref), 1.0)
        print(lps(sample, ref))

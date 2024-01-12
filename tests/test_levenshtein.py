from unittest import TestCase
from Levenshtein import distance
from lps.lps import LevenshteinPhonemeSimilarity
import torchaudio
import soundfile as sf


class TestLevenshtein(TestCase):
    def test_levenshtein(self):
        self.assertEqual(distance("foo", "nooo"), 2)

    def test_levenshtein_sim(self):
        (ref, _), (sample, _) = torchaudio.load("resources/speech.wav"), torchaudio.load("resources/speech_bab_0dB.wav")
        lps = LevenshteinPhonemeSimilarity()
        ref = ref.numpy()
        sample = sample.numpy()
        self.assertEqual(lps(ref, ref), 1.0)
        self.assertLess(lps(ref, sample), 1.0)

from unittest import TestCase
from src.lps.helloworld import hello


class TestHello(TestCase):
    def test_hello(self):
        self.assertEqual(0, hello())

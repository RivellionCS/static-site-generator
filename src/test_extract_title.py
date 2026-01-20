import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_h1(self):
        title = extract_title("# Hello")
        self.assertEqual(title, "Hello")

    def test_indented_h1(self):
        title = extract_title(" # Indented Title ")
        self.assertEqual(title, "Indented Title")

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            extract_title("")

    def test_not_a_title(self):
        with self.assertRaises(ValueError):
            extract_title("## Not an h1")

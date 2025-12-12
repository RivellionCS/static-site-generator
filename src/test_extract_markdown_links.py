import unittest
from extract_markdown_links import extract_markdown_links

class test_extract_markdown_links(unittest.TestCase):
    def test_one_link(self):
        matches = extract_markdown_links(
            "This is a link to [google](https://www.google.com)"
        )
        self.assertEqual([("google", "https://www.google.com")], matches)

    def test_image_and_link(self):
        matches = extract_markdown_links(
            "This is a [link](https://www.google.com) and ![image](https://www.images.com/image.png)"
        )
        self.assertEqual([("link", "https://www.google.com")], matches)

    def test_multiple_links(self):
        matches = extract_markdown_links(
            "This is one [link](https://www.google.com) and this is [another](https://www.brave.com)"
        )
        self.assertEqual([("link", "https://www.google.com"), ("another", "https://www.brave.com")], matches)

    def test_link_with_spaces(self):
        matches = extract_markdown_links(
            "Check this [cool search engine](https://www.google.com)"
        )
        self.assertEqual(
            [("cool search engine", "https://www.google.com")],
            matches,
        )
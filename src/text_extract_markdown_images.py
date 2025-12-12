import unittest
from extract_markdown_images import extract_markdown_images

class text_extract_markdown_images(unittest.TestCase):
    def test_one_image(self):
        matches = extract_markdown_images(
            "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_image_and_link(self):
        matches = extract_markdown_images(
            "This is a [link](https://www.google.com) and ![image](https://www.images.com/image.png)"
        )
        self.assertEqual([("image", "https://www.images.com/image.png")], matches)

    def test_multiple_images(self):
        matches = extract_markdown_images(
            "This is one [image](https://www.images.com/image01.png) and two [image1](https://www.images.com/image02.png)"
        )
        self.assertEqual([("image", "https://www.images.com/image01.png"), ("image1", "https://www.images.com/image02.png")], matches)


    def test_link_with_spaces(self):
        matches = extract_markdown_images(
            "Check this [cool image picture](https://www.images.com/image.png)"
        )
        self.assertEqual(
            [("cool search engine", "https://www.images.com/image.png")],
            matches,
        )
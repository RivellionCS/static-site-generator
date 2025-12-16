import unittest
from split_nodes_image import split_nodes_image
from textnode import TextNode, TextType

class test_split_nodes_image(unittest.TestCase):
    def test_two_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_no_image(self):
        node = TextNode(
            "This is text with no images",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is text with no images", TextType.TEXT)], new_nodes
        )

    def test_with_link_and_images(self):
        node = TextNode(
            "This is text with one ![image](image.png) and a [link][www.google.com]",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with one ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "image.png"),
                TextNode(" and a [link][www.google.com]", TextType.TEXT)
            ],
            new_nodes
        )

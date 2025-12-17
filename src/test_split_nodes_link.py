import unittest
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

class test_split_nodes_link(unittest.TestCase):
    def test_links(self):
        node = TextNode("this is a [link](https://www.google.com) and this is also a [link](https://www.bing.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("this is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and this is also a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.bing.com")
            ],
            new_nodes
        )

    def test_no_link(self):
        node = TextNode("this is text without any links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [node],
            new_nodes
        )
    
    def test_images_and_links(self):
        node = TextNode("This is a text with a [link](https://www.google.com) and an ![image](image.png)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and an ![image](image.png)", TextType.TEXT),
            ],
            new_nodes
        )
import unittest
from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter

class test_split_nodes_delimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is a text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "This is a text with a ")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " word")

    def test_italic(self):
        node = TextNode("This is a text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0], TextNode("This is a text with an ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("italic", TextType.ITALIC))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))

    def test_code(self):
        node = TextNode("This is a text with `code` in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0], TextNode("This is a text with ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" in it", TextType.TEXT))

    def test_exception(self):
        node = TextNode("This text should throw an **exception", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_multiple(self):
        node = TextNode("This is a text with **multiple** words that are **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0], TextNode("This is a text with ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("multiple", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(" words that are ", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("bold", TextType.BOLD))

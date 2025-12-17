import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class test_text_to_textnodes(unittest.TestCase):
    def test_with_every_text_type(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) with some extra text"
        node_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" with some extra text", TextType.TEXT)
            ],
            node_list
        )
    
    def test_bold(self):
        text = "some text with a **bold** word"
        node_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("some text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ],
            node_list
        )
    
    def test_italic(self):
        text = "some text with an _italic_ word"
        node_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("some text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT)
            ],
            node_list
        )
    
    def test_code(self):
        text = "some text with `code` in it"
        node_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("some text with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" in it", TextType.TEXT)
            ],
            node_list
        )
    
    def test_link(self):
        text = "some text with a [link](www.google.com) in it"
        node_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("some text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "www.google.com"),
                TextNode(" in it", TextType.TEXT)
            ],
            node_list
        )
    
    def test_image(self):
        text = "some text with an ![image](image.png) in it"
        node_list = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("some text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "image.png"),
                TextNode(" in it", TextType.TEXT)
            ],
            node_list
        )
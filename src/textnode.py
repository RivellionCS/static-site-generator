from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINKS = "link"
    IMAGES = "image"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node1, node2):
        return node1.text == node2.text and node1.text_type == node2.text_type and node1.url == node2.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

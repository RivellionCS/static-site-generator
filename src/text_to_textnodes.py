from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_link import split_nodes_link
from split_nodes_image import split_nodes_image

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    split_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    split_italic = split_nodes_delimiter(split_bold, "_", TextType.ITALIC)
    split_code = split_nodes_delimiter(split_italic, "`", TextType.CODE)
    split_links = split_nodes_link(split_code)
    split_images = split_nodes_image(split_links)
    return split_images
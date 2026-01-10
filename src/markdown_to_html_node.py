from block_to_block_type import block_to_block_type, BlockType
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node
from parentnode import ParentNode
from textnode import TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    node_list = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_tag = None
        block_children = None
        if block_type == BlockType.PARAGRAPH:
            block_tag = "p"
            block_children = paragraph_block_to_html_node(block)
        elif block_type == BlockType.HEADING:
            heading_count = block.count('#')
            block_tag = f"h{heading_count}"
            block_children = heading_block_to_html_node(block, heading_count)
        elif block_type == BlockType.CODE:
            block_tag = "pre"
            block_children = code_block_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            block_tag = f"blockquote"
            block_children = quote_block_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            block_tag = f"ul"
            block_children = unordered_list_block_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            block_tag = f"ol"
            block_children = ordered_list_block_to_html_node(block)
        else:
            raise TypeError(f"Error: cannot convert {block_type} to html tag")
        block_node = ParentNode(block_tag, block_children)
        node_list.append(block_node)
    final_node = ParentNode("div", node_list)
    return final_node

def paragraph_block_to_html_node(block):
    return text_to_children(block.replace("\n", " "))

def heading_block_to_html_node(block, heading_count):
    filtered_text = block[heading_count + 1:]
    return text_to_children(filtered_text)

def code_block_to_html_node(block):
    filtered_text = block[3:-3]
    if len(filtered_text) > 1 and filtered_text[0] == "\n":
        filtered_text = filtered_text.lstrip("\n")
    code_text_node = text_node_to_html_node(TextNode(filtered_text, TextType.TEXT))
    parent_node = ParentNode("code", [code_text_node])
    return [parent_node]

def quote_block_to_html_node(block):
    split_text = block.split("\n")
    filtered_lines = []
    for line in split_text:
        filtered_lines.append(line[2:])
    filtered_text = "\n".join(filtered_lines)
    return text_to_children(filtered_text)

def unordered_list_block_to_html_node(block):
    split_text = block.split("\n")
    nodes = []
    for line in split_text:
        nodes.append(ParentNode("li", text_to_children(line[2:])))
    return nodes

def ordered_list_block_to_html_node(block):
    split_text = block.split("\n")
    nodes = []
    for line in split_text:
        index = line.find(".")
        nodes.append(ParentNode("li", text_to_children(line[index + 2:])))
    return nodes

def text_to_children(text):
    text_node_list = text_to_textnodes(text)
    html_node_list = []
    for node in text_node_list:
        html_node_list.append(text_node_to_html_node(node))
    return html_node_list
from extract_markdown_links import extract_markdown_links
from textnode import TextType, TextNode

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links_list = extract_markdown_links(node.text)
        if len(links_list) == 0:
            new_nodes.append(node)
            continue
        node_text = node.text
        for link in links_list:
            link_text = link[0]
            link_url = link[1]
            sections = node_text.split(f"[{link_text}]({link_url})", 1)
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))


    return new_nodes
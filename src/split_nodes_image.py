from extract_markdown_images import extract_markdown_images
from textnode import TextType, TextNode

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images_list = extract_markdown_images(node.text)
        if len(images_list) == 0:
            new_nodes.append(node)
            continue
        node_text = node.text
        for image in images_list:
            image_alt = image[0]
            image_link = image[1]
            sections = node_text.split(f"![{image_alt}]({image_link})", 1)
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))


    return new_nodes
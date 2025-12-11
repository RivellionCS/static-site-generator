from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if delimiter not in old_node.text:
            new_nodes.append(old_node)
            continue

        count = old_node.text.count(delimiter)
        if count % 2 != 0:
            raise ValueError(f"Error: uneven amount of delimiter {delimiter}")
        
        temp_list = old_node.text.split(delimiter)
        for i in range(len(temp_list)):
            if temp_list[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(temp_list[i], TextType.TEXT))
            elif i % 2 == 1:
                new_nodes.append(TextNode(temp_list[i], text_type))

    return new_nodes
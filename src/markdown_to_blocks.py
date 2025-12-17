
def markdown_to_blocks(markdown):
    block = []
    split_text = markdown.split("\n\n")
    for text in split_text:
        stripped_text = text.strip()
        if stripped_text != "":
            block.append(stripped_text)
    return block
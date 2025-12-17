from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.match(r'^#{1,6}\s+.+', block):
        return BlockType.HEADING
    if re.match(r'^```.*```$', block):
        return BlockType.CODE
    if re.match(r'^(>.*\n?)+$', block):
        return BlockType.QUOTE
    if re.match(r'^(?:-.*(?:\n|$))+', block):
        return BlockType.UNORDERED_LIST
    split_lines = block.splitlines()
    expected_number = 1
    valid = True

    for line in split_lines:
        match = re.match(r'^(\d+)\. .+', line)
        if not match:
            valid = False
            break
        number = int(match.group(1))
        if number != expected_number:
            valid = False
            break
        expected_number += 1
    if valid:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
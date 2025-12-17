import unittest
from block_to_block_type import BlockType, block_to_block_type

class test_block_to_block_type(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code_block(self):
        block = "```This is a code block```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote_block(self):
        block = ">This is a quote block\n>With multiple lines"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- This is a list\n- With multiple\n- Elements"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        block = "1. This is an ordered list\n2. with multiple\n3. Elements"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_improper_ordered_list(self):
        block = "1. This is a fake ordered list\n1. with multiple\n2. Elements"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = "This is a simple paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
import unittest
from markdown_to_blocks import markdown_to_blocks

class test_markdown_to_blocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
        
        def test_markdown_to_blocks_empty(self):
            md = ""
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])

        def test_markdown_to_blocks_single_block(self):
             md = "This is a single block"
             blocks = markdown_to_blocks(md)
             self.assertEqual(blocks, ["This is a single block"])

        def test_markdown_to_blocks_whitespaces(self):
             md = "    This is a block with trailing whitespaces    "
             blocks = markdown_to_blocks(md)
             self.assertEqual(blocks, ["This is a block with trailing whitespaces"])

        def test_markdown_to_blocks_newlines_only(self):
             md = "\n\n\n"
             blocks = markdown_to_blocks(md)
             self.assertEqual(blocks, [])
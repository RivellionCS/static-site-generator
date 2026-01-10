import unittest
from markdown_to_html_node import markdown_to_html_node

class test_markdown_to_html_node(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_empty(self):
        md = """"""
        
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div></div>"
        )

    def test_single_heading_block(self):
        md = """
# This is a heading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1></div>"
        )
    
    def test_single_paragraph_block(self):
        md = """
This is a paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph</p></div>"
        )
    
    def test_single_code_block(self):
        md = """
```
This is code
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is code\n</code></pre></div>"
        )

    def test_paragraph_leading_and_trailing_spaces(self):
        md = """
   This is a paragraph with leading and trailing spaces   
""" 

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph with leading and trailing spaces</p></div>"
        )

    def test_heading_levels(self):
        md = """
# This

## Is

### A Heading

#### With

##### Multiple

###### Levels
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This</h1><h2>Is</h2><h3>A Heading</h3><h4>With</h4><h5>Multiple</h5><h6>Levels</h6></div>"
        )

    def test_heading_with_inline(self):
        md = """
# This is a Heading with **bold** _italic_ and `code` elements
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a Heading with <b>bold</b> <i>italic</i> and <code>code</code> elements</h1></div>"
        )

    def test_heading_count_number(self):
        md = """
####### This should be a paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>####### This should be a paragraph</p></div>"
        )

    def test_code_block_with_literals(self):
        md = """
```
This is code with **bold** and _italic_
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is code with **bold** and _italic_\n</code></pre></div>"
        )

    def test_empty_code_block(self):
        md = """```
```"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>\n</code></pre></div>"
        )

    def test_single_quote(self):
        md = """
> This is a quote.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote.</blockquote></div>"
        )

    def test_multiple_quotes(self):
        md = """
> This is the first line.
> This is the second line.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is the first line.\nThis is the second line.</blockquote></div>"
        )

    def test_partial_empty_quote(self):
        md = """
> First line
> 
> Third line
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>First line\n\nThird line</blockquote></div>"
        )

    def test_unordered_list(self):
        md = """
- Item 1
- **Item 2**
- _Item 3_
- `Item 4`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li><b>Item 2</b></li><li><i>Item 3</i></li><li><code>Item 4</code></li></ul></div>"
        )

    def test_unordered_list_empty_elements(self):
        md = """
- Item 1
- 
- Item 2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li></li><li>Item 2</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. Item 1
2. **Item 2**
3. _Item 3_
4. `Item 4`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li><b>Item 2</b></li><li><i>Item 3</i></li><li><code>Item 4</code></li></ol></div>"
        )

    def test_full_document(self):
        md = """
# Main Heading

This is a paragraph with **bold** text.

- Item 1
- Item 2

1. Object 1
2. Object 2

```
some_code()
```

Another paragraph with _italic_ text.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Main Heading</h1><p>This is a paragraph with <b>bold</b> text.</p><ul><li>Item 1</li><li>Item 2</li></ul><ol><li>Object 1</li><li>Object 2</li></ol><pre><code>some_code()\n</code></pre><p>Another paragraph with <i>italic</i> text.</p></div>"
        )
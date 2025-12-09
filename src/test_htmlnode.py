import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_self(self):
        node = HTMLNode("<a>", "google", None, {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("<p>", "hello world", None, {"id": "test", "class": "plain"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
        self.assertEqual(repr(node), "HTMLNode(<a>, google, None, {'href': 'https://www.google.com', 'target': '_blank'})")
        self.assertEqual(node2.props_to_html(), 'id="test" class="plain"')
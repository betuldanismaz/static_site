import unittest
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.example.com" target="_blank"')
    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello World")
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=Hello World, children=[], props={})")
    def test_no_value_or_children(self):
        node = HTMLNode(tag="div")
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=None, children=[], props={})")

if __name__ == '__main__':
    unittest.main()

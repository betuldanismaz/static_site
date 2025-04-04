import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_textnode_inequality_different_text(self):
        node1 = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_textnode_inequality_different_text_type(self):
        node1 = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Sample text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_textnode_inequality_different_url(self):

        node1 = TextNode("Sample text", TextType.LINK, "https://example.com")
        node2 = TextNode("Sample text", TextType.LINK, "https://another.com")
        self.assertNotEqual(node1, node2)

    def test_textnode_default_url(self):

        node = TextNode("Sample text", TextType.LINK)
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()

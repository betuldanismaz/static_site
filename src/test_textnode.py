import unittest
from src.textnode import TextNode, TextType
from src.textnode_to_html_node import text_node_to_html_node, LeafNode

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

    # Additional test cases
    def test_textnode_to_html_text(self):
        node = TextNode("This is a plain text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)  # Assuming this should be None
        self.assertEqual(html_node.value, "This is a plain text")

    def test_textnode_to_html_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_textnode_to_html_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_textnode_to_html_code(self):
        node = TextNode("This is code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text")

    def test_textnode_to_html_link(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props["href"], "https://example.com")

    def test_textnode_to_html_image(self):
        node = TextNode("Image description", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "https://example.com/image.jpg")
        self.assertEqual(html_node.props["alt"], "Image description")

    def test_invalid_type(self):
        # Using an invalid TextType value
        node = TextNode("Invalid type", "INVALID_TYPE")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()

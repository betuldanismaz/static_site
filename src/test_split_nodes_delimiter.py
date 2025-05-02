import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter  # Fonksiyonun bulunduğu dosya

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text, " word")

    def test_bold(self):
        node = TextNode("This is **bolded text** inside", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "bolded text")
        self.assertEqual(new_nodes[2].text, " inside")

    def test_italic(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[2].text, " text")

    def test_multiple_delimiters(self):
        node = TextNode("This is a `code` and **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This is a ")
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[3].text, "bold")
        self.assertEqual(new_nodes[4].text, " text")

    def test_invalid_delimiter(self):
        node = TextNode("This is invalid `code block", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()

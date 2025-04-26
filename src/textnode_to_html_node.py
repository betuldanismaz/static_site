from enum import Enum

class TextType(Enum):
    TEXT = "text"
    LINK = "link"
    IMAGE = "image"
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


# Modify this function to handle all valid text types
def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected a TextNode")

    if text_node.text_type == TextType.TEXT:
        # Handle plain text node, no tag
        return LeafNode(value=text_node.text, tag=None)

    elif text_node.text_type == TextType.BOLD:
        # Handle bold text, wrap in <b> tag
        return LeafNode(value=text_node.text, tag="b")

    elif text_node.text_type == TextType.ITALIC:
        # Handle italic text, wrap in <i> tag
        return LeafNode(value=text_node.text, tag="i")

    elif text_node.text_type == TextType.CODE:
        # Handle code text, wrap in <code> tag
        return LeafNode(value=text_node.text, tag="code")

    elif text_node.text_type == TextType.LINK:
        # Handle link text, wrap in <a> tag
        if text_node.url:
            return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
        else:
            raise Exception("URL is required for LINK type")

    elif text_node.text_type == TextType.IMAGE:
        # Handle image text, wrap in <img> tag
        if text_node.url:
            return LeafNode(value=text_node.text, tag="img", props={"src": text_node.url, "alt": text_node.text})
        else:
            raise Exception("URL is required for IMAGE type")

    else:
        # If the text type is not recognized, raise an exception
        raise Exception("Invalid text type")


# Define LeafNode (update as necessary)
class LeafNode:
    def __init__(self, value, tag=None, props=None):
        self.value = value
        self.tag = tag
        self.props = props if props else {}

    def __repr__(self):
        return f"LeafNode(value={self.value}, tag={self.tag}, props={self.props})"


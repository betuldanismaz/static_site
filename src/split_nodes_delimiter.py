from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid Markdown syntax: unmatched delimiter")

        for i in range(len(parts)):
            if i % 2 == 0:
                # Normal metin
                if parts[i]:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                # Delimiter içindeki metin
                new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes


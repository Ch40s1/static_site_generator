from htmlnode import LEAFNODE

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

# text_node is a dict { text: "hello": text_type: "bold"}


def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LEAFNODE(None, text_node.text)
    elif text_node.text_type == text_type_bold:
        return LEAFNODE('b', text_node.text)
    elif text_node.text_type == text_type_italic:
        return LEAFNODE('i', text_node.text)
    elif text_node.text_type == text_type_link:
        return LEAFNODE('a', text_node.text, {'href': text_node.url})
    elif text_node.text_type == text_type_code:
        return LEAFNODE('code', text_node.text)
    elif text_node.text_type == text_type_image:
        return LEAFNODE('img', "", {'src': text_node.url}, {'alt': text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    # I created variables like text_type_text="text" and text_type_code="code" to represent the various valid TextNode types.
    # If an "oldnode" is not a TextNode, you should just add it to the new list as-is, we only attempt to split TextNode objects.
    # If a matching closing delimter is not found, just raise an exception with a helpful error message, that's invalid Markdown syntax.
    # The .split() method was useful to me
    # The .extend() method was useful to me
    pass

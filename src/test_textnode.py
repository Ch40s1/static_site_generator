import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is node", "bold")
        node2 = TextNode("This is node", "bold")
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is text node", "bold")
        node2 = TextNode("This is text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is text node", "bold", "google.com")
        node2 = TextNode("This is text node", "italic", "boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def text_textnode_to_htmlnode(self):
        node = TextNode("This is image", "image", "google.com")
        self.assertEqual(node.text_node_to_html_node(),
                         '<img src="google.com" alt="This is image"></img>')

    if __name__ == "__main__":
        unittest.main()

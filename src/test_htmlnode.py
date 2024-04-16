import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(None, None, None, {
                        "href": "boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(),
                         ' href="boot.dev" target="_blank"')

    def test_leaf_toHtml(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(),
                         "<p>This is a paragraph of text.</p>"
                         )

    def test_leafwProps(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),
                         '<a href="https://www.google.com">Click me!</a>'
                         )

    def test_parentnode_toHtml(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),
                         "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


if __name__ == "__main__":
    unittest.main()

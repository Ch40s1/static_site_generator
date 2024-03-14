# import unittest from python library
import unittest

# import the class we are testig
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    # create two textnode objects with the same properties and asserts that they are equal
    def test_eq(self):
        node = TextNode('This is a text node', "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        # Test inequality when text is different
        node = TextNode('This is a text node', "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_type(self):
        # Test inequality when text_type is different
        node = TextNode('This is a text node', "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_not_eq_none_url(self):
        # Test inequality when url is None for one object
        node = TextNode('This is a text node', "bold", "http://example.com")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node, node2)

    def test_eq_same_url(self):
        # Test equality when urls are the same
        node = TextNode('This is a text node', "bold", "http://example.com")
        node2 = TextNode("This is a text node", "bold", "http://example.com")
        self.assertEqual(node, node2)

    def test_not_eq_different_url(self):
        # Test inequality when urls are different
        node = TextNode('This is a text node', "bold", "http://example.com")
        node2 = TextNode("This is a text node", "bold", "http://another-example.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

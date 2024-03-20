import unittest
from htmlnode import HTMLNODE, LEAFNODE, PARENTNODE


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = PARENTNODE(
            "p",
            [
                LEAFNODE("b", "Bold text"),
                LEAFNODE(None, "Normal text"),
                LEAFNODE("i", "italic text"),
                LEAFNODE(None, "Normal text"),
            ],
        )
        node.to_html()


if __name__ == "__main__":
    unittest.main()

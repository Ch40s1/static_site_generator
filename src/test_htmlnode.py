import unittest

from htmlnode import HTMLNODE


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNODE(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )


if __name__ == "__main__":
    unittest.main()

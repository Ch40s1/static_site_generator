import unittest
from htmlnode import LEAFNODE, PARENTNODE, HTMLNODE


class TestHTMLNODE(unittest.TestCase):
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

    def test_to_html_no_children(self):
        node = LEAFNODE("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LEAFNODE(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LEAFNODE("span", "child")
        parent_node = PARENTNODE("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LEAFNODE("b", "grandchild")
        child_node = PARENTNODE("span", [grandchild_node])
        parent_node = PARENTNODE("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = PARENTNODE(
            "p",
            [
                LEAFNODE("b", "Bold text"),
                LEAFNODE(None, "Normal text"),
                LEAFNODE("i", "italic text"),
                LEAFNODE(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = PARENTNODE(
            "h2",
            [
                LEAFNODE("b", "Bold text"),
                LEAFNODE(None, "Normal text"),
                LEAFNODE("i", "italic text"),
                LEAFNODE(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()

import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            "a",
            "Hello Monday. Welcome to the good life",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            '<a  href="https://www.google.com" target="_blank">Hello Monday. Welcome to the good life</a>',
            repr(node),
        )

    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            node = HTMLNode("p", "Hello Monday")
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Hello Monday. Welcome to the good life",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )

    def test_values(self):
        node = HTMLNode("div", "Hello World")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, None)
        self.assertEqual(node.value, "Hello World")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_tag(self):
        text = "This is a plain text Joe. No Tag"

        node = LeafNode(None, text)
        self.assertEqual(node.to_html(), text)

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a",
            "Google it",
            {
                "href": "https://www.google.com",
            },
        )

        self.assertEqual(
            '<a href="https://www.google.com">Google it</a>', node.to_html()
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

        def test_headings(self):
            node = ParentNode(
                "h2",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            self.assertEqual(
                node.to_html(),
                "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
            )


if __name__ == "__main__":
    unittest.main()

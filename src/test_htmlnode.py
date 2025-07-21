import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    #def test_eq(self):
    #    node = TextNode("This is a text node", TextType.BOLD)
    #    node2 = TextNode("This is a text node", TextType.BOLD)
    #    self.assertEqual(node, node2)
    def test_repr(self):
        node = HTMLNode("a", "Google", None, {"href": "https://www.google.com"})
        self.assertEqual(repr(node), f"HTMLNode(a, Google, children: None, {{'href': 'https://www.google.com'}})")
        

    def test_props_to_html(self):
        node = HTMLNode("a", "Google", None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\"")


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_leaf_to_html_a_props(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click Me!</a>")


    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello World")
        self.assertEqual(node.to_html(), "Hello World")


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

if __name__ == "__main__":
    unittest.main()
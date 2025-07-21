import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def text_neq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


    def test_linktypo(self):
        node = TextNode("This is a link node", TextType.LINKS, "https://www.google.com")
        node2 = TextNode("This is a link node", TextType.LINKS, "https://ww.google.com")
        self.assertNotEqual(node, node2)
        

    def test_texttypo(self):
        node = TextNode("This is text node", TextType.CODE)
        node2 = TextNode("This is a test node", TextType.CODE)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()

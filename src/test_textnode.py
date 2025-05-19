import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_ineq(self):
      node = TextNode("This is a bold node", TextType.BOLD)
      node2 = TextNode("This is a text node", TextType.NORMAL)
      self.assertNotEqual(node, node2)
    
    def test_link_node(self):
      with self.assertRaises(Exception):
        TextNode("This is a link node", TextType.LINK)
      


if __name__ == "__main__":
    unittest.main()
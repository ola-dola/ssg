import unittest 
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
  def test_repr(self):
    node = HTMLNode("a", "Hello Monday. Welcome to the good life", None, {
        "href": "https://www.google.com",
        "target": "_blank",
      }
    )
    self.assertEqual(
      '<a  href="https://www.google.com" target="_blank">Hello Monday. Welcome to the good life</a>', 
      repr(node))
  
  def test_to_html(self):
    with self.assertRaises(NotImplementedError):
      node = HTMLNode('p', 'Hello Monday')
      node.to_html()
  
  def test_props_to_html(self):
    node = HTMLNode("a", "Hello Monday. Welcome to the good life", None, {
        "href": "https://www.google.com",
        "target": "_blank",
      }
    )
    
    self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())
    
  def test_values(self):
    node = HTMLNode('div', 'Hello World')
    self.assertEqual(node.tag, 'div')
    self.assertEqual(node.children, None)
    self.assertEqual(node.value, 'Hello World')
  
if __name__ == "__main__":
    unittest.main()
    
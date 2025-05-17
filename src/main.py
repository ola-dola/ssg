from textnode import TextNode, TextType

def main():
  link = TextNode("This is some anchor text", TextType.LINK, "https://www.google.com")
  print(link)

main()

from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        if text_type == TextType.LINK and url is None:
            raise Exception("Url is required for link nodes. Otherwise use normal text")

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return isinstance(other, TextNode) and (
            self.text,
            self.text_type,
            self.url,
        ) == (other.text, other.text_type, other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode): 
    html_node = None

    match text_node.text_type:
        case TextType.TEXT:
            html_node = LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            html_node = LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            html_node = LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            html_node = LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            html_node = LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            html_node = LeafNode(
                tag="img",
                value="",
                props={"src": text_node.url, "alt": text_node.text},
            )
        case _:
            raise ValueError("Invalid text node type")
        
    return html_node

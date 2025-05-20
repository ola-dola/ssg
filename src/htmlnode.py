class HTMLNode():
  def __init__(self, tag: str = None, value: str =None, children=None, props: dict = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    if self.props is None:
      return ""
    
    attribute = " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    return f" {attribute}"
  
  def __repr__(self):
    return f"<{self.tag} {self.props_to_html()}>{self.value if self.value else self.children}</{self.tag}>"


class LeafNode(HTMLNode):
  def __init__(self, tag: str | None, value: str, props=None):
    super().__init__(tag=tag, value=value, children=None, props=props)
  
  def to_html(self):
    if self.value is None:
      raise ValueError("Value cannot be None")
    
    if self.tag is None:
      return self.value
    
    return f"<{self.tag}{self.props_to_html()}>{self.value if self.value else self.children}</{self.tag}>"
  
  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
  def __init__(self, tag, children: list, props = None):
    super().__init__(tag=tag, value=None, children=children, props=props)
    
  def to_html(self):
    if self.tag is None:
      raise ValueError("ParentNode must have a tag")
    
    if self.children is None:
      raise ValueError("Parent node must have child(ren)")
    
    inner_html = ""
    
    for child in self.children:
      inner_html += child.to_html()
    
    return f"<{self.tag}>{inner_html}</{self.tag}>"
    
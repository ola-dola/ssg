class HTMLNode():
  def __init__(self, tag: str = None, value: str =None, children=None, props: dict = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    if not self.props:
      return ""
    
    attribute = " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    return f" {attribute}"
  
  def __repr__(self):
    return f"<{self.tag} {self.props_to_html()}>{self.value if self.value else self.children}</{self.tag}>"


class LeafNode(HTMLNode):
  def __init__(self, tag: str | None, value, props=None):
    super().__init__(tag=tag, value=value, children=None, props=props)
  
  def to_html(self):
    if not self.value:
      raise ValueError("Value cannot be None")
    
    if not self.tag:
      return self.value
    
    return f"<{self.tag}{self.props_to_html()}>{self.value if self.value else self.children}</{self.tag}>"
  
  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"
class HTMLNode():
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    attr = " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    return f" {attr}"
  
  def __repr__(self):
    return f"<{self.tag} {self.props_to_html()}>{self.value if self.value else self.children}</{self.tag}>"

    
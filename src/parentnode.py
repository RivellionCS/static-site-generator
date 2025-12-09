from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Error: tag value is None")
        if self.children is None:
            raise ValueError("Error: children value is None")
        else:
            if self.props:
                string = f"<{self.tag} {self.props_to_html()}>"
            else:
                string = f"<{self.tag}>"
            for child in self.children:
                string += child.to_html()
            string += f"</{self.tag}>"
            return string


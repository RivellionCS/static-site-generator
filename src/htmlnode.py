class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_self(self):
        if self.props == None or not self.props:
            return ""
        string = ""
        for prop in self.props:
            string += f'{prop}="{self.props[prop]}" '
        return string.strip()
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
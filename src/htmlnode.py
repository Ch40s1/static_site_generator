class HTMLNODE:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to be determined")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"html tag:{self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

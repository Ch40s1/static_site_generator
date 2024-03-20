class HTMLNODE:
    # define the contructor of the main node
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # method to turn the node into html
    def to_html(self):
        pass

    # the props to html method
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    # print method return the value of the html
    def __repr__(self):
        return f"html tag:{self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"


class LEAFNODE(HTMLNODE):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: requires a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class PARENTNODE(HTMLNODE):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        # create an empty string
        children_html = ""
        # recursively call the method on each children and add the return f"" if it has no more children
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"PARENTNODE({self.tag}, children: {self.children}, {self.props})"

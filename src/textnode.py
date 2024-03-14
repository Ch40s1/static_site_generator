#define class
class TextNode:
    # initial contructor with instance variables
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # eq method to test id two objects are equal
    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    # string representation method
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

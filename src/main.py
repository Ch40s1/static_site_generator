# import the class from the textnode file
from textnode import TextNode


def main():
    # create node with dummy data
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)


main()

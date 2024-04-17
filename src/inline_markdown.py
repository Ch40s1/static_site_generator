import re

from textnode import (
    TextNode,
    text_type_image,
    text_type_link,
    text_type_code,
    text_type_italic,
    text_type_text,
    text_type_bold,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    # go thtough list
    for node in old_nodes:
        # if node is not text append to new nodes
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        # make new list for split nodes
        split_nodes = []
        sections = node.text.split(delimiter)
        # check length for odd number, split old_nodes will be odd because of split section
        if len(sections) % 2 == 0:
            raise ValueError("Not formatted correctly")
        # loop though new list with range of its length
        for i in range(len(sections)):
            # if a section is "" continue
            if sections[i] == "":
                continue
            # if the secntion is the second part add tp new list with TextNode format
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

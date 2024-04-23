# import re

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
    blocks_list = []
    # loop through lines in section  with split
    for line in markdown.split("\n\n"):
        # figure out if line is empty
        if line == "":
            # if it is continue to next part
            continue
        # append the current block to list
        line = line.strip()
        # else add line to current block
        blocks_list.append(line)
    # return the list
    return blocks_list


def block_to_block_type(block):
    lines = block.split("\n")

    # Check for heading
    if block.startswith("# "):
        return block_type_heading

    # Check for code block
    if len(lines) > 2 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code

    # Check for quote
    if block.startswith(">"):
        return block_type_quote

    # Check for unordered list
    if any(line.startswith("- ") for line in lines):
        return block_type_ulist

    # Check for ordered list
    if any(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return block_type_olist

    # Default to paragraph
    return block_type_paragraph


def markdown_to_html(markdown):
    # split in a list of block to work with
    blocks = markdown_to_blocks(markdown)
    # empty list to hold the children of the div
    children = []
    # loop over
    for block in blocks:
        # html node var is called to determine the type of block
        html_node = block_to_block_type(block)
        # append to children list after formatted
        children.append(html_node)
    # return ParentNode
    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    # split lines at the new line
    lines = block.split("\n")
    # join the lines into one whole paragraph
    paragraph = " ".join(lines)
    # get formatted children
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code blocl")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def quote_to_html_node(block):
    lines = block.split("\n")
    new_line = []
    for line in lines:
        if not line.startwith(">"):
            raise ValueError("Invalid quote block")
        new_line.append(line.lstrip(">").strip())
    content = " ".join(new_line)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

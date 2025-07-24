import re

from enum import Enum

class Blocktype(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    ULIST = "unordered_list",
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return Blocktype.HEADING
    elif block.startswith('```') and block.endswith('```'):
        return Blocktype.CODE
    elif block.startswith('>'):
        for line in block.split('\n'):
            if not line.startswith('>'):
                return Blocktype.PARAGRAPH
        return Blocktype.QUOTE
    elif block.startswith('- '):
        for line in block.split('\n'):
            if not line.startswith('- '):
                return Blocktype.PARAGRAPH
        return Blocktype.ULIST
    elif block.startswith("1. "):
        block_spl = block.split('\n')
        for i in range(len(block_spl)):
            if not block_spl[i].startswith(f"{i + 1}. "):
                return Blocktype.PARAGRAPH
        return Blocktype.OLIST
    else:
        return Blocktype.PARAGRAPH

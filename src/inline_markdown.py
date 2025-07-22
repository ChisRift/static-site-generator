import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for node in old_nodes:
     if node.text_type != TextType.TEXT:
        new_nodes.append(node)
     else:
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
           raise Exception("uneven delimiters counted in text")
        for i in range(len(split_text)):
           if i % 2 == 0:
              new_nodes.append(TextNode(split_text[i], TextType.TEXT))
           else:
              new_nodes.append(TextNode(split_text[i], text_type))
  return new_nodes

def extract_markdown_images(text):
   matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
   #matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
   return matches

def extract_markdown_links(text):
   #(?<!!) - Negative lookback. Cannot match character after ?<!
   matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
   #matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
   return matches
from textnode import TextType
from textnode import TextNode

def main():
  # print("hello world")
  new_node = TextNode("some random text", TextType.BOLD)
  print(repr(new_node))


main()

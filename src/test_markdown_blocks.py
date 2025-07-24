import unittest

from markdown_blocks import Blocktype, markdown_to_blocks, block_to_block_type

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        #print(blocks)
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items"
        ]
        self.assertListEqual(blocks, expected)
    
    def test_block_to_block_type_header(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        expected = Blocktype.HEADING
        self.assertEqual(block_type, expected)
    
    def test_block_to_block_type_header2(self):
        block = "#### This is also a heading"
        block_type = block_to_block_type(block)
        expected = Blocktype.HEADING
        self.assertEqual(block_type, expected)
    
    def test_block_to_block_type_header_neq(self):
        block = "#This is not a valid heading"
        block_type = block_to_block_type(block)
        expected = Blocktype.HEADING
        self.assertNotEqual(block_type, expected)
    
    def test_block_to_block_type_header_neq2(self):
        block = "####### This is also not a valid heading"
        block_type = block_to_block_type(block)
        expected = Blocktype.HEADING
        self.assertNotEqual(block_type, expected)
    
    def test_block_to_block_type_ulist(self):
        block = "- This is a list\n- with items"
        block_type = block_to_block_type(block)
        expected = Blocktype.ULIST
        self.assertEqual(block_type, expected)
    
    def test_block_to_block_type_ulist_neq(self):
        block = "- This is a list\n- with items\n but not all with a -"
        block_type = block_to_block_type(block)
        expected = Blocktype.ULIST
        self.assertNotEqual(block_type, expected)
    
    def test_block_to_block_type_olist(self):
        block = "1.This is a list\n2.with items"
        block_type = block_to_block_type(block)
        expected = Blocktype.OLIST
        self.assertEqual(block_type, expected)
    
    def test_block_to_block_type_olist(self):
        block = "1.This is a list\n2 with items"
        block_type = block_to_block_type(block)
        expected = Blocktype.OLIST
        self.assertNotEqual(block_type, expected)
    
    def test_block_to_block_type_code(self):
        block = "```This is code text```"
        block_type = block_to_block_type(block)
        expected = Blocktype.CODE
        self.assertEqual(block_type, expected)
    
    def test_block_to_block_type_code_multiline(self):
        block = "```This is code text\non multiple lines```"
        block_type = block_to_block_type(block)
        expected = Blocktype.CODE
        self.assertEqual(block_type, expected)
    
    def test_block_to_block_type_code_fewer_backticks(self):
        block = "```This is code text without the right amount of backticks``"
        block_type = block_to_block_type(block)
        expected = Blocktype.CODE
        self.assertNotEqual(block_type, expected)
    
    def test_block_to_block_type_code_more_backticks(self):
        block = "`````This is code text without the right amount of backticks````"
        block_type = block_to_block_type(block)
        expected = Blocktype.CODE
        self.assertEqual(block_type, expected)
    
    def test_block_to_block_type_quote(self):
        block = ">This is a quote block\n>And more quotes"
        block_type = block_to_block_type(block)
        expected = Blocktype.QUOTE
        self.assertEqual(block_type, expected)
    
    def test_block_to_block_type_quote_neq(self):
        block = ">This is a quote block\n>And more quotes\nBut not all flagged correctly"
        block_type = block_to_block_type(block)
        expected = Blocktype.QUOTE
        self.assertNotEqual(block_type, expected)


if __name__ == "__main__":
    unittest.main()
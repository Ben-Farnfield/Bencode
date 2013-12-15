#! /usr/bin/python

from bencode_parser import tokenizer
from bencode_parser import BencodeSyntaxError

import unittest

class TestBencodeTokenizer(unittest.TestCase):

    def test_int(self):
        self.next_token = tokenizer("i10e").next
        self.assertEqual("i",  self.next_token())
        self.assertEqual("10", self.next_token())
        self.assertEqual("e",  self.next_token())

    def test_str(self):
        self.next_token = tokenizer("5:Hello").next
        self.assertEqual("s",     self.next_token())
        self.assertEqual("Hello", self.next_token())

    def test_list(self):
        self.next_token = tokenizer("le").next
        self.assertEqual("l", self.next_token())
        self.assertEqual("e", self.next_token())

    def test_dict(self):
        self.next_token = tokenizer("de").next
        self.assertEqual("d", self.next_token())
        self.assertEqual("e", self.next_token())

    def test_raise_exception_if_char_not_in_alphabet(self):
        self.next_token = tokenizer("a").next
        try:
            self.assertRaises(BencodeSyntaxError, self.next_token())
        except BencodeSyntaxError:
            pass

    # Test to check for non-ASCII chars

if __name__=="__main__":
    unittest.main()
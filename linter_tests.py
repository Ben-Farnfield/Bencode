#! /usr/bin/python

import linter

import unittest

class TestBint(unittest.TestCase):
    
    def test_val_bint_i10e(self):
        self.bint = linter.val_bint('i10e', 0)
        self.assertTrue(self.bint['result'])
        self.assertEquals(self.bint['pointer'], 4)

    def test_val_bint_i10ee(self):
        self.bint = linter.val_bint('i10ee', 0)
        self.assertTrue(self.bint['result'])
        self.assertEquals(self.bint['pointer'], 4)

    def test_inval_bint_ii10e(self):
        self.bint = linter.val_bint('ii10e', 0)
        self.assertFalse(self.bint['result'])
        self.assertEquals(self.bint['pointer'], 0)

    def test_inval_bint_ie10e(self):
        self.bint = linter.val_bint('ie10e', 0)
        self.assertFalse(self.bint['result'])
        self.assertEquals(self.bint['pointer'], 0)

    def test_inval_bint_5hello(self):
        self.bint = linter.val_bint('5:hello', 0)
        self.assertFalse(self.bint['result'])
        self.assertEquals(self.bint['pointer'], 0)

    def test_inval_bint_le(self):
        self.bint = linter.val_bint('le', 0)
        self.assertFalse(self.bint['result'])
        self.assertEquals(self.bint['pointer'], 0)

    def test_inval_bint_de(self):
        self.bint = linter.val_bint('de', 0)
        self.assertFalse(self.bint['result'])
        self.assertEquals(self.bint['pointer'], 0)


class TestBstr(unittest.TestCase):

    def test_val_bstr_5hello(self):
        self.bstr = linter.val_bstr('5:hello', 0)
        self.assertTrue(self.bstr['result'])
        self.assertEquals(self.bstr['pointer'], 7)

    def test_inval_bstr_5hell(self):
        self.bstr = linter.val_bstr('5:hell', 0)
        self.assertFalse(self.bstr['result'])
        self.assertEquals(self.bstr['pointer'], 0)

    def test_inval_bstr_i10e(self):
        self.bstr = linter.val_bstr('i10e', 0)
        self.assertFalse(self.bstr['result'])
        self.assertEquals(self.bstr['pointer'], 0)

    def test_inval_bstr_le(self):
        self.bstr = linter.val_bstr('le', 0)
        self.assertFalse(self.bstr['result'])
        self.assertEquals(self.bstr['pointer'], 0)

    def test_inval_bstr_de(self):
        self.bstr = linter.val_bstr('de', 0)
        self.assertFalse(self.bstr['result'])
        self.assertEquals(self.bstr['pointer'], 0)


class TestBlist(unittest.TestCase):

    def test_val_blist_le(self):
        self.blist = linter.val_blist('le', 0)
        self.assertTrue(self.blist['result'])
        self.assertEquals(self.blist['pointer'], 2)

    def test_val_blist_llee(self):
        self.blist = linter.val_blist('llee', 0)
        self.assertTrue(self.blist['result'])
        self.assertEquals(self.blist['pointer'], 4)

    def test_val_blist_llleee(self):
        self.blist = linter.val_blist('llleee', 0)
        self.assertTrue(self.blist['result'])
        self.assertEquals(self.blist['pointer'], 6)

    def test_val_blist_li10ee(self):
        self.blist = linter.val_blist('li10ee', 0)
        self.assertTrue(self.blist['result'])
        self.assertEquals(self.blist['pointer'], 6)

    def test_val_blist_l5helloe(self):
        self.blist = linter.val_blist('l5:helloe', 0)
        self.assertTrue(self.blist['result'])
        self.assertEquals(self.blist['pointer'], 9)

    def test_val_blist_ldee(self):
        pass

    def test_val_blist_li10e5helloe(self):
        self.blist = linter.val_blist('li10e5:hell0e', 0)
        self.assertTrue(self.blist['result'])
        self.assertEquals(self.blist['pointer'], 13)

    def test_inval_blist_lle(self):
        self.blist = linter.val_blist('lle', 0)
        self.assertFalse(self.blist['result'])
        self.assertEquals(self.blist['pointer'], 3)




if __name__=="__main__":
    unittest.main()

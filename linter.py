#! /usr/bin/python

import re

def int_fa(bcode, i):

    table = {'A' : {'i':'B'},
             'B' : {'\d':'C'},
             'C' : {'\d':'D', 'e':None},
             'D' : {'\d':'D', 'e':None}}

    state = 'A'
    while state is not None:
        char = bcode[i]
        if char.isdigit():
            char = '\d'
        try:
            state = table[state][char]
            i += 1
        except KeyError:
            return (False, i)
    return (True, i)

def str_fa(bcode, i):
    pass

def lint(bcode):
    print int_fa(bcode, 0)

lint('i1000000e')
lint('5:hello')

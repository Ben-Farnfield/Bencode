#! /usr/bin/python

import re

def val_bint(bcode, pointer):

    m = re.compile(r"(i\d+e)").match(bcode, pointer)
    if m is None:
        return {'result':False, 'pointer':pointer} # not a bencoded int
    return {'result':True, 'pointer':m.end(m.lastindex)}


def val_bstr(bcode, pointer):

    m = re.compile(r"(?P<str_len>\d+)(?P<str_start>:)").match(bcode, pointer)
    if m is None:
        return {'result':False, 'pointer':pointer} # not a bencoded string
    str_len = int(m.group('str_len'))
    str_start = m.end('str_start')
    str_end = str_start + str_len
    if str_end <= len(bcode):
        return {'result':True, 'pointer':str_end} 
    else:
        return {'result':False, 'pointer':pointer}


def val_blist(bcode, pointer):

    table = {'A' : {'l':'B'},
             'B' : {'bint':'C','bstr':'D','blist':'E','bdict':'F'},
             'C' : {'bint':'C','bstr':'D','blist':'E','bdict':'F'},
             'D' : {'bint':'C','bstr':'D','blist':'E','bdict':'F'},
             'E' : {'bint':'C','bstr':'D','blist':'E','bdict':'F'},
             'F' : {'bint':'C','bstr':'D','blist':'E','bdict':'F'}}

    state = 'A'
    inside_blist = False

    while True:
        try:
            char = bcode[pointer]
        except IndexError:
            return {'result':False, 'pointer':pointer}

        if char == 'l' and inside_blist == False:
            pointer += 1
            inside_blist = True
        elif char != 'l' and inside_blist == False:
            return {'result':False, 'pointer':pointer}
        elif char == 'e' and inside_blist == True:
            pointer += 1
            return {'result':True, 'pointer':pointer}
        else:
            bint = val_bint(bcode, pointer)
            bstr = val_bstr(bcode, pointer)
            blist = val_blist(bcode, pointer)
            bdict = val_bdict(bcode, pointer)

            if bint['result']:
                char = 'bint'
                pointer = bint['pointer']
            elif bstr['result']:
                char = 'bstr'
                pointer = bstr['pointer']
            elif blist['result']:
                char = 'blist'
                pointer = blist['pointer']
            elif bdict['result']:
                char = 'bdict'
                pointer = bdict['pointer']
            else:
                pass # RAISE ERROR

        try:
            state = table[state][char]
        except KeyError:
            return {'result':False, 'pointer':pointer}


def val_bdict(bcode, pointer):
    return {'result':False, 'pointer':pointer}


def val_bencode(bcode):
    pass


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
            if bint['result']:
                pointer = bint['pointer']
                continue

            bstr = val_bstr(bcode, pointer)
            if bstr['result']:
                pointer = bstr['pointer']
                continue

            blist = val_blist(bcode, pointer)
            if blist['result']:
                pointer = blist['pointer']
                continue

            bdict = val_bdict(bcode, pointer)
            if bdict['result']:
                pointer = bdict['pointer']
                continue

            else:
                return {'result':False, 'pointer':pointer}


def val_bdict(bcode, pointer):
    return {'result':False, 'pointer':pointer}


def val_bencode(bcode):
    pass


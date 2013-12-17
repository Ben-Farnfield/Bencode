import re
import sys

class BencodeSyntaxError(Exception):
    """ """
    def __init__(self, msg=""):
        Exception.__init__(self, msg) 

    def __str__(self):
        return "Invalid Bencode syntax found"


# Function to tokenize a bencoded string
#
# Arguments:
#           bcode       string containing bencoded data
# Yield:
#           Yields one token for each call to next(). These tokens are 
#           'i' 'e' 'l' 'd' integer or string.
#
def tokenizer(bcode):
    match = re.compile(r"([ield])|(?P<str_len>\d+):|(-?\d+)").match

    pointer = 0
    while pointer < len(bcode):
        m = match(bcode, pointer)

        if m is None:
            raise BencodeSyntaxError

        e = m.end(m.lastindex)

        if m.lastindex == 2:
            yield "s"
            str_start = e + 1 # move pointer passed ':'
            str_end = str_start + int(m.group("str_len"))
            yield bcode[str_start:str_end]
            pointer = str_end
        else:
            yield m.group(m.lastindex)
            pointer = e


def builder(next_token, token):
    builders = {"s" : _build_string,
                "i" : _build_int,
                "l" : _build_list,
                "d" : _build_dict}
    try:
        return builders[token](next_token)
    except KeyError:
        raise BencodeSyntaxError

def _build_string(next_token):
    """ """
    return next_token()

def _build_int(next_token):
    """ """
    built_int = int(next_token())
    if next_token() != "e":
        raise BencodeSyntaxError
    return built_int

def _build_list(next_token):
    """ """
    built_list = []
    token = next_token()
    while token != "e":
        built_list.append(builder(next_token, token))
        token = next_token()
    return built_list

def _build_dict(next_token):
    """ """
    built_dict = {}
    token = next_token()
    while token != "e":
        key = builder(next_token, token)
        token = next_token()
        val = builder(next_token, token)
        built_dict[key] = val
        token = next_token()
    return built_dict


def decoded_bencode(bcode):
    """ """
    next_token = tokenizer(bcode).next

    while True:
        try:
            token = next_token()
            yield builder(next_token, token)
        except StopIteration:
            break
        except BencodeSyntaxError as e:
            sys.stderr.write(str(e))
            raise

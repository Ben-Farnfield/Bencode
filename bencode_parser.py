import sys

class BencodeSyntaxError(Exception):
    """ """
    def __init__(self, msg=""):
        Exception.__init__(self, msg) 

    def __str__(self):
        return "Invalid Bencode syntax found"


def tokenizer(bcode):
    """ """
    integer = ""
    pointer = 0

    while pointer < len(bcode):

        char = bcode[pointer]
        
        if char in ("i","d","l","e"): # match all basic tags
            yield char
            pointer += 1
            continue

        while True:
            if  _is_int(char):  # match int
                integer += char # store char from int
                pointer += 1
                char = bcode[pointer]
                continue
            
            if char == "e": # match end of int
                yield integer
                yield "e"
                pointer += 1
                integer = ""
                break

            if char == ":": # match start of string
                yield "s"
                pointer += 1
                yield bcode[pointer:pointer+int(integer)] # extract string
                pointer += int(integer) # move pointer to end of string
                integer = ""
                break
            else:
                raise BencodeSyntaxError  # char not in alphabet


def _is_int(char):
    """ Returns True if passed a string representing a valid int """
    try:
        int(char)
        return True
    except:
        return False


def builder(next_token, token):
    """ """
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

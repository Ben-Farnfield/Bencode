#! /usr/bin/python

def tokenizer(bcode):
    integer = ""
    pointer = 0

    while pointer < len(bcode):

        char = bcode[pointer]
        
        if char in ("i","d","l","e"): # match all basic tags
            yield char
            pointer += 1
            continue
        
        while True:
            if char not in ("e",":"): # match integer
                integer += char # store char from integer
                pointer += 1
                char = bcode[pointer]
                continue
            
            if char == "e": # match end of integer
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
                

def builder(next, token):
    item = None

    if token == "s":
        item = next()

    elif token == "i":
        item = int(next())
        if next() != "e":
            print "SyntaxError(item)"

    elif token == "l":
        item = []
        token = next()
        while token != "e":
            item.append(builder(next, token))
            token = next()

    elif token == "d":
        item = {}
        token = next()
        while token != "e":
            key = builder(next, token)
            token = next()
            val = builder(next, token)
            item[key] = val
            token = next()
            
    return item


def decoded_bencode(bcode):
    next = tokenizer(bcode).next
    while True:
        try:
            token = next()
            yield builder(next, token)
        except StopIteration:
            break


with open("/home/mooli/Downloads/crunchbang-11-20130506-amd64.iso.torrent", "r") as f:
    dot_torrent = f.read()

print list(item for item in decoded_bencode(dot_torrent))

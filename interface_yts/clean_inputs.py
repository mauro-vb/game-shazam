def no_empty(list):
    return ([i for i in list if i != ""])

def only_num(inp):
    res ="".join(x for x in inp if  x.isdecimal())
    return res

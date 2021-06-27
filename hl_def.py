syn = {
    "in": "void",
    "out": "void",
    "dupe": "void",
    "del": "void",
    "inc": "void", 
    "dec": "void", 
    "add": "void",
    "sub": "void", 
    "mul": "void", 
    "div": "void", 
    "mod": "void", 
    "jmp": "label", 
    "jez": "label", 
    "jlz": "label", 
    "jgz": "label", 
    "jnz": "label", 
    "load": "register", 
    "save": "register",
    # these commands don't get turned into opcodes
    "label": "label", 
    "note" : "void",
    # for debug and puzzle creation, not for players
    "lit": "num",
    "lits": "nums",
    "rand": "void",
    "out_all": "void", # outputs entire stack
}

registers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z']
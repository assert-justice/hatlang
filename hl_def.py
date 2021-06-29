syn = {
    "in": {"arg":"void", "pops": 0}, # pops a value from the inbox and pushes it to the stack
    "out": {"arg":"void", "pops": 1}, # pops a value from the stack and pushes it to the outbox
    "dupe": {"arg":"void", "pops": 1}, # duplicates the top item from the stack and pushes it
    "del": {"arg":"void", "pops": 1}, # deletes the top item from the stack
    "zero": {"arg":"void", "pops": 0}, # pushes a zero to the stack
    "rand": {"arg":"void", "pops": 0}, # pushes a random number from -999 to 999 inclusive to the stack
    "inc": {"arg":"void", "pops": 1}, # increments the value at the top of the stack
    "dec": {"arg":"void", "pops": 1}, # decrements the value at the top of the stack
    "add": {"arg":"void", "pops": 2}, # pops two items from the stack, adds them, and pushes the result
    "sub": {"arg":"void", "pops": 2}, 
    "mul": {"arg":"void", "pops": 2}, 
    "div": {"arg":"void", "pops": 2}, 
    "mod": {"arg":"void", "pops": 2}, 
    "jmp": {"arg":"label", "pops": 0}, # unconditional jump to label
    "jez": {"arg":"label", "pops": 0}, # if the top value of the stack is zero jump to the label. does not change the stack
    "jlz": {"arg":"label", "pops": 0}, # jump less than zero
    "jgz": {"arg":"label", "pops": 0}, # jump greater than zero
    "jnz": {"arg":"label", "pops": 0}, # jump if not zero
    "load": {"arg":"register", "pops": 0}, # get the value from a register and push it
    "save": {"arg":"register", "pops": 1}, # pop a value from the stack and save it to a register
    "swp": {"arg":"void", "pops": 2}, # pops two values and pushes them back in the opposite order
    "srt": {"arg":"label", "pops": 0}, # jump to subroutine
    "ret": {"arg":"void", "pops": 0}, # return from subroutine
    "sln": {"arg":"void", "pops": 0}, # pushes the size of the stack (before the instruction) to the stack
    # these commands don't get turned into opcodes
    "label": {"arg":"label", "pops": 0}, 
    "note" : {"arg":"void", "pops": 0},
    # for debug and puzzle creation, not for players
    "lit": {"arg":"num", "pops": 0}, # pushes a literal number to the stack
    "lits": {"arg":"nums", "pops": 0}, # pushes several literal numbers to the stack. parser turns it into a series of lit instructions
    "out_all": {"arg":"void", "pops": 0}, # outputs entire stack
    "print": {"arg":"void", "pops": 1}, # prints the top value of the stack to the console
    "dump": {"arg":"void", "pops": 0}, # prints the state of the interpreter at that point
}

registers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z']
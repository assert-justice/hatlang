'''
Hatlang
A reference implimentation for the language in Hatstack

'''
from hl_def import *
def parse(src: str):
    lines = [line.split(' ') for line in src.splitlines()]
    program = []
    labels = {}
    has_error = False
    def error(message, num_line):
        nonlocal has_error
        has_error = True
        print(message, 'on line {}'.format(line_num))
    def valid(line_num, line):
        op = line[0]
        if not op in syn:
            error('unrecognized command \'{}\''.format(op), line_num)
            return
        arg = syn[op]
        if arg == 'void':
            return [op, 0, '', line_num]
        elif len(line) < 2:
            error('opcode \'{}\' expects a {}'.format(op, arg), line_num)
            return
        else:
            if arg == 'label':
                return [op, 0, line[1], line_num]
            elif arg == 'register':
                if line[1] in registers:
                    return [op, registers.index(line[1]), '', line_num]
                else:
                    error('register name \'{}\' not recognized'.format(line[1]), line_num)
                    return
            elif arg == 'num':
                return [op, int(line[1]), '', line_num]
            elif arg == 'nums':
                return [op, 0, ' '.join(line[1:]), line_num]

    for line_num, line in enumerate(lines):
        if len(line[0]) == 0:
            continue
        line = valid(line_num, line)
        if has_error:
            return
        op, _, s, ln = line
        if op == 'label':
            if s in labels:
                error('label {} is already defined'.format(s), line_num)
                return
            labels[s] = len(program)
        elif op == 'lits':
            lits = s.split(' ')
            for lit in lits:
                program.append(['lit', int(lit), '', ln])
        else:
            program.append(line)
    # resolve labels
    for i, inst in enumerate(program):
        op, _, s, ln = inst
        if syn[op] == 'label':
            if not s in labels:
                error('label \'{}\' is not defined'.format(s), ln)
                return
            program[i][1] = labels[s]
    return program
            
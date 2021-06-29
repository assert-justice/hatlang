from hl_def import syn
import random

def interpret(program, inbox = None, status = None, valid = None):
    def_status = {
        "has_error": False,
        "error_msg": "",
        "cycles": 0,
        "max_cycles": -1,
        "register_use": 0,
        "max_size": 0,
        "debug": False
    }
    if status == None:
        status = {}
    for d in def_status:
        status.setdefault(d, def_status[d])
    if inbox == None:
        inbox = []
    else:
        inbox = inbox[:]
    stack = []
    outbox = []
    cstack = [] # call stack used for macros
    reg = [0 for _ in range(8)]
    # cycles = 0
    # max_cycles = 10_000
    def error(message, ln):
        status['has_error'] = True
        status['error_msg'] = message + ' on line ' + str(ln)
        print(status['error_msg'])
    def bin(f):
        b = stack.pop()
        a = stack.pop()
        stack.append(f(a,b))
    def dump():
        print('\nprogram dump')
        print('inbox', inbox)
        print('stack', stack)
        print('outbox', outbox)
        print('registers', reg)
    def verify():
        if not valid:
            return True
        return valid[:len(outbox)] == outbox
        

    while reg[7] < len(program):
        if reg[7] >= len(program):
            reg[7] = 0
        ip = reg[7]
        op, num, _, ln = program[ip]
        if status['debug']:
            print(op)
        pops = syn[op]['pops']
        status['cycles'] += 1
        if status['cycles'] == status['max_cycles']:
            error('maximum cycles reached', ln)
            break
        if len(stack) < pops:
            error('cannot execute instruction \'{}\': stack must have {} values it has {}'.format(op, pops, len(stack)), ln)
            break
        if op == 'in':
            if len(inbox) == 0:
                break
            stack.append(inbox.pop())
        elif op == 'out':
            outbox.append(stack.pop())
            if not verify():
                error('incorrect value \'{}\' in outbox'.format(outbox[-1]), ln)
                break
        elif op == 'dupe':
            stack.append(stack[-1])
        elif op == 'del':
            stack.pop()
        elif op == 'zero':
            stack.append(0)
        elif op == 'rand':
            stack.append(random.randint(-999, 999))
        elif op == 'inc':
            stack[-1] += 1
        elif op == 'dec':
            stack[-1] -= 1
        elif op == 'add':
            bin(lambda a,b: a+b)
        elif op == 'sub':
            bin(lambda a,b: a-b)
        elif op == 'mul':
            bin(lambda a,b: a*b)
        elif op == 'div':
            bin(lambda a,b: a//b)
        elif op == 'mod':
            bin(lambda a,b: a%b)
        elif op == 'jmp':
            ip = num
        elif op == 'jez':
            if stack[-1] == 0:
                ip = num
        elif op == 'jlz':
            if stack[-1] < 0:
                ip = num
        elif op == 'jgz':
            if stack[-1] > 0:
                ip = num
        elif op == 'jnz':
            if stack[-1] != 0:
                ip = num
        elif op == 'load':
            status['register_use'] += 1
            stack.append(reg[num])
        elif op == 'save':
            status['register_use'] += 1
            reg[num] = stack.pop()
        elif op == 'swp':
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif op == 'srt':
            cstack.append(ip + 1)
            ip = num
        elif op == 'ret':
            if len(cstack) == 0:
                error('cannot return, call stack is empty!', ln)
            else:
                ip = cstack.pop()
        elif op == 'sln':
            stack.append(len(stack))
        elif op == 'lit':
            stack.append(num)
        elif op == 'out_all':
            while len(stack) > 0:
                outbox.append(stack.pop())
        elif op == 'print':
            print(stack[-1])
        elif op == 'dump':
            dump()
        else:
            print('opcode {} not implimented'.format(op))
        
        if len(stack) > status['max_size']:
            status['max_size'] = len(stack)
        
        if ip == reg[7]:
            reg[7] += 1
        else:
            reg[7] = ip
    if valid and valid != outbox:
        error('not enough items in the inbox!', 0)
    # if status['has_error']:
    #     dump()
    return outbox
        
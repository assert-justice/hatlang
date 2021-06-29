# parses puzzles and verifies solutions

import hl_parse, hl_interp

def parse_puzzle(text):
    preludes = []
    impls = []
    #best_impl_speed = 1000000
    desc = []
    puzzle = {
        'preludes' : [],
        'impls': [],
        'desc': ''
        # 'best_impl': [],
        # 'best_size' : 0,
        # 'best_speed': 0,
        # 'best_reg_use': 0,
        # 'best_stack_size': 0,
    }
    mode = 'none'
    for line in text.splitlines():
        line = line.strip()
        if line.find('#desc') == 0:
            mode = 'desc'
        elif line.find('#pre') == 0:
            mode = 'pre'
            preludes.append([])
        elif line.find('#impl') == 0:
            mode = 'impl'
            impls.append([])
        else:
            if mode == 'pre':
                preludes[-1].append(line)
            elif mode == 'impl':
                impls[-1].append(line)
            elif mode == 'desc':
                desc.append(line)
    puzzle['desc'] = '\n'.join(desc)
    preludes = [hl_parse.parse('\n'.join(pre)) for pre in preludes]
    impls = [hl_parse.parse('\n'.join(impl)) for impl in impls]
    #print(preludes)
    #print(impls)
    # statuses = [{} for _ in impls]
    # for pre in preludes: 
    #     inbox = hl_interp.interpret(pre)
    #     for i, impl in enumerate(impls):
    #         hl_interp.interpret(impl, inbox, statuses[i])
    #         if statuses[i]['cycles'] < best_impl_speed:
    #             best_impl_speed = statuses[i]['cycles']
    #             puzzle['best_impl'] = impl
    # puzzle['best_size'] = min([len(impl) for impl in impls])
    # puzzle['best_speed'] = min([status['cycles'] for status in statuses])
    # puzzle['best_reg_use'] = min([status['register_use'] for status in statuses])
    # puzzle['best_stack_size'] = min([status['max_size'] for status in statuses])
    puzzle['preludes'] = preludes
    puzzle['impls'] = impls
    return puzzle

def validate(puzzle, solution):
    statuses = [{} for _ in puzzle['impls']]
    solution_status = {}
    for pre in puzzle['preludes']:
        inbox = hl_interp.interpret(pre)
        print(inbox)
        outs = [hl_interp.interpret(impl, inbox, statuses[i]) for i, impl in enumerate(puzzle['impls'])]
        print(outs[0])
        outbox = hl_interp.interpret(solution, inbox, solution_status, outs[0])
        if solution_status['has_error']:
            print('solution failed on input: ' + str(inbox))
            print('expected outbox: ' + str(outs[0]))
            print('actual outbox: ' + str(outbox))
            return False
    results = {
        'cycles' : solution_status['cycles'],
        'register_use': solution_status['register_use'],
        'max_stack_size': solution_status['max_size'],
        'num_instructions': len(solution),
        'best_cycles': min([status['cycles'] for status in statuses]),
        'best_register_use': min([status['register_use'] for status in statuses]),
        'best_max_stack_size': min([status['max_size'] for status in statuses]),
        'best_num_instructions': min([len(impl) for impl in puzzle['impls']]),
    }
    return results
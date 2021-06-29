'''
Hatlang
A reference implimentation for the language in Hatstack

'''
import hl_parse, hl_interp, hl_verify, hl_puzzle, sys

def parse(fname):
    text = open(fname).read()
    return hl_parse.parse(text)

# pre = parse('pre_test.hat')
# ref = parse('test_impl.hat')
# prog = parse('test.hat')
# ver = hl_verify.verify(pre, ref, prog)
# print(ver)
# status = {}
# print(hl_interp.interpret(parse('scripts/fib.hat'), [30], status))
# print(status)
puzzle = hl_puzzle.parse_puzzle(open('puzzles/avgn.hp').read())
print(puzzle['desc'])
solution = parse('scripts/avgn.hat')
val = hl_puzzle.validate(puzzle, solution)
if val:
    print('passing all tests!')
    for key in val:
        print(key, val[key])
else:
    print('try again')
# s = {}
# out = hl_interp.interpret(parse('scripts/avgn.hat'), [20, 10, 2], s)
# print(out)
#print(s)

# def main():
#     if len(sys.argv) == 1:
#         print('not enough commands supply a source file')
#         return
#     fname = sys.argv[1]
#     f = open(fname)
#     text = f.read()
#     f.close()

#     program = hl_parse.parse(text)
#     # for inst in program:
#     #     print(inst)
#     status = {}
#     out = hl_interp.interpret(program, inbox=[10], status=status)
#     print(out)
#     print(status)

# main()
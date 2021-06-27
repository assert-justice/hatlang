'''
Hatlang
A reference implimentation for the language in Hatstack

'''
import hl_parse, sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('not enough commands supply a source file')
    else:
        fname = sys.argv[1]
        f = open(fname)
        text = f.read()
        f.close()

        program = hl_parse.parse(text)
        for inst in program:
            print(inst)
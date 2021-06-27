from hl_def import *

def interpret(inbox, program):
    stack = []
    outbox = []
    reg = [0 for _ in range(8)]

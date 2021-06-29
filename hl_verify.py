import hl_interp

def verify(prelude, ref_impl, program):
    inbox = hl_interp.interpret(prelude)
    ref_outbox = hl_interp.interpret(ref_impl, inbox)
    status = {}
    outbox = hl_interp.interpret(program, inbox, status, ref_outbox)
    return not status['has_error'], status
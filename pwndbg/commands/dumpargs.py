#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import pwndbg.commands
import pwndbg.arguments
import pwndbg.disasm

@pwndbg.commands.Command
@pwndbg.commands.OnlyWhenRunning
def dumpargs(*a):
    """
    If the current instruction is a call instruction, print that arguments.
    """
    result = []

    # For call instructions, attempt to resolve the target and
    # determine the number of arguments.
    for arg, value in pwndbg.arguments.get(pwndbg.disasm.one()):
        code   = False if arg.type == 'char' else True
        pretty = pwndbg.chain.format(value, code=code)
        result.append('%8s%-10s %s' % ('',arg.name+':', pretty))

    print('\n'.join(result))

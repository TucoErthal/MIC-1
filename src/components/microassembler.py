from .microinstruction_register import *

mir = MicroinstructionRegister()
mir.input = lambda: microinstruction(cond = 3)
mir.debug()
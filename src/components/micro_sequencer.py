from .bit_types import *

class MicroSequencer:
    def __init__(self):
        self.input_cond : Bit2 = Bit2(0)
        self.input_negative_flag : Bit1 = Bit1(0)
        self.input_zero_flag : Bit1 = Bit1(0)

    @property
    def output(self) -> Bit1:
        match(self.input_cond._value):            
            case 0b00: # no branch
                return Bit1(0)
            case 0b01: # branch if NEG
                return Bit1(self.input_negative_flag._value)
            case 0b10: # branch if ZERO
                return Bit1(self.input_zero_flag._value)
            case 0b10: # branch
                return Bit1(1)
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
"""
A do MMux é o increment
B do mmux é o ADDR da microinstrução
"""
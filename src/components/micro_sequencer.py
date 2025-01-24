from .bit_types import *

class MicroSequencer:
    def input_cond(self) -> Bit2:
        raise ConnectionError("Input unconnected")

    def input_negative_flag(self) -> Bit1:
        raise ConnectionError("Input unconnected")

    def input_zero_flag(self) -> Bit1:
        raise ConnectionError("Input unconnected")

    def output(self) -> Bit1:
        _input_cond = self.input_cond()
        _input_negative_flag = self.input_negative_flag()
        _input_zero_flag = self.input_zero_flag()
        
        match(_input_cond.unsigned):            
            case 0b00: # no branch
                return Bit1(0)
            
            case 0b01: # branch if NEG
                return Bit1(_input_negative_flag.unsigned)
            
            case 0b10: # branch if ZERO
                return Bit1(_input_zero_flag.unsigned)
            
            case 0b10: # branch
                return Bit1(1)
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
"""
A do MMux é o increment
B do mmux é o ADDR da microinstrução
"""
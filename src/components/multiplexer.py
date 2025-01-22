from .bit_types import *

class Multiplexer16by2:
    def __init__(self):
        self.input_A : Bit16 | Bit16 = Bit16(0)
        self.input_B : Bit16 | Bit16 = Bit16(0)
        self.select : Bit1 = Bit1(0)

    @property
    def output(self) -> Bit16 | Bit16:
        match(self.select._value):
            case 0:
                return self.input_A
            
            case 1: 
                return self.input_B
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
            
class Multiplexer8by2:
    def __init__(self):
        self.input_A : Bit8 = Bit8(0)
        self.input_B : Bit8 = Bit8(0)
        self.select : Bit1 = Bit1(0)

    @property
    def output(self) -> Bit8 | Bit8:
        match(self.select._value):
            case 0:
                return self.input_A
            
            case 1: 
                return self.input_B
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
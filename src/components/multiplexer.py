from .bit_types import *

class Multiplexer16by2:
    def __init__(self):
        self.input_A : Int16 | UInt16 = Int16(0)
        self.input_B : Int16 | UInt16 = Int16(0)
        self.select : Bit1 = Bit1(0)

    @property
    def output(self) -> Int16 | UInt16:
        match(self.select.value):
            case 0:
                return self.input_A
            
            case 1: 
                return self.input_B
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
            
class Multiplexer8by2:
    def __init__(self):
        self.input_A : UInt8 = UInt8(0)
        self.input_B : UInt8 = UInt8(0)
        self.select : Bit1 = Bit1(0)

    @property
    def output(self) -> UInt8 | UInt8:
        match(self.select.value):
            case 0:
                return self.input_A
            
            case 1: 
                return self.input_B
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
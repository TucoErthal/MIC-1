from .bit_types import *

class Multiplexer16by2:
    def __init__(self):
        self.A : Int16 = Int16(0)
        self.B : Int16 = Int16(0)
        self.select : UInt1 = UInt1(0)

    @property
    def output(self) -> Int16:
        match(self.select.value):
            case 0:
                return self.A
            
            case 1: 
                return self.B
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
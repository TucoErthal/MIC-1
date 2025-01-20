from .bit_types import *

class ArithmeticLogicUnit:
    """
    F = 00: R = A + B
    F = 01: R = A & B
    F = 10: R = A
    F = 11: R = INV(A)
    """
    def __init__(self):
        self.opcode : UInt4 = UInt4(0)
        self.A : Int16 = Int16(0)
        self.B : Int16 = Int16(0)

    @property
    def output(self) -> Int16:
        match(self.opcode.value):
            case 0b00: # ADD
                return Int16(self.A.value + self.B.value)
            
            case 0b00: # AND
                return Int16(self.A.value & self.B.value)
            
            case 0b00: # PASS
                return Int16(self.A.value)
            
            case 0b00: # NOT
                return Int16(~ self.A.value)
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
            
    @property
    def zero_flag(self) -> UInt1:
        return UInt1(1) if self.A.value + self.B.value == 0 else UInt1(0)
    
    @property
    def negative_flag(self):
        return UInt1(1) if self.A.value + self.B.value < 0 else UInt1(0)
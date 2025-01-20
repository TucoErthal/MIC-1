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
        self.input_A : Int16 | UInt16 = Int16(0)
        self.input_B : Int16 | UInt16 = Int16(0)

    @property
    def output(self) -> Int16 | UInt16:
        match(self.opcode.value):
            case 0b00: # ADD
                return Int16(self.input_A.value + self.input_B.value)
            
            case 0b01: # AND
                return Int16(self.input_A.value & self.input_B.value)
            
            case 0b10: # PASS
                return Int16(self.input_A.value)
            
            case 0b11: # NOT
                return Int16(~ self.input_A.value)
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
            
    @property
    def zero_flag(self) -> UInt1:
        return UInt1(1) if self.input_A.value + self.input_B.value == 0 else UInt1(0)
    
    @property
    def negative_flag(self):
        return UInt1(1) if self.input_A.value + self.input_B.value < 0 else UInt1(0)
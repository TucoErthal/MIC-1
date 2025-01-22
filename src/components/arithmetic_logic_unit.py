from .bit_types import *

class ArithmeticLogicUnit:
    """
    F = 00: R = A + B
    F = 01: R = A & B
    F = 10: R = A
    F = 11: R = INV(A)
    """
    def __init__(self):
        self.opcode : Bit2 = Bit2(0)
        self.input_A : Bit16 = Bit16(0)
        self.input_B : Bit16 = Bit16(0)

    @property
    def output(self) -> Bit16:
        match(self.opcode.unsigned):
            case 0b00: # ADD
                return Bit16((self.input_A.unsigned + self.input_B.unsigned) % (1 << 16))
            
            case 0b01: # AND
                return Bit16(self.input_A.unsigned & self.input_B.unsigned)
            
            case 0b10: # PASS
                return Bit16(self.input_A.unsigned)
            
            case 0b11: # NOT
                return Bit16(~ self.input_A.unsigned)
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
            
    @property
    def zero_flag(self) -> Bit1:
        return Bit1(1) if self.input_A.unsigned + self.input_B.unsigned == 0 else Bit1(0)
    
    @property
    def negative_flag(self):
        return Bit1(1) if self.input_A.unsigned + self.input_B.unsigned < 0 else Bit1(0)
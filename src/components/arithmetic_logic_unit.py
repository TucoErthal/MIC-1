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
                _output = Bit16((self.input_A.unsigned + self.input_B.unsigned) % (1 << 16))
                if VERBOSE_DEBUG: print(f"\talu.add({self.input_A.unsigned}, {self.input_B.unsigned}) = {_output.unsigned}")
                return _output
            
            case 0b01: # AND
                _output = Bit16(self.input_A.unsigned & self.input_B.unsigned)
                if VERBOSE_DEBUG: print(f"\talu.and({self.input_A.unsigned}, {self.input_B.unsigned}) = {_output.unsigned}")
                return _output
            
            case 0b10: # PASS
                _output = Bit16(self.input_A.unsigned)
                if VERBOSE_DEBUG: print(f"\talu.pass({self.input_A.unsigned}) = {_output.unsigned}")
                return _output
            
            case 0b11: # NOT
                _output = Bit16(~ self.input_A.unsigned)
                if VERBOSE_DEBUG: print(f"\talu.not({self.input_A.unsigned}) = {_output.unsigned}")
                return _output
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
            
    @property
    def zero_flag(self) -> Bit1:
        return Bit1(1) if self.input_A.unsigned + self.input_B.unsigned == 0 else Bit1(0)
    
    @property
    def negative_flag(self):
        return Bit1(1) if self.input_A.unsigned + self.input_B.unsigned < 0 else Bit1(0)
    
def test():
    print("TEST 1: arithmetic logic unit")
    alu1 = ArithmeticLogicUnit()
    alu1.input_A = Bit16(8)
    alu1.input_B = Bit16(90)

    alu2 = ArithmeticLogicUnit()
    alu2.input_A = alu1.output
    alu2.input_B = Bit16(5)
    alu2.output
from .bit_types import *

class ArithmeticLogicUnit:
    """
    F = 00: R = A + B
    F = 01: R = A & B
    F = 10: R = A
    F = 11: R = INV(A)
    """
    def opcode(self) -> Bit2:
        raise ConnectionError("Input unconnected")

    def input_A(self) -> Bit16:
        raise ConnectionError("Input unconnected")

    def input_B(self) -> Bit16:
        raise ConnectionError("Input unconnected")

    def output(self) -> Bit16:
        _opcode = self.opcode()
        _input_A = self.input_A()
        _input_B = self.input_B()

        match(_opcode.unsigned):

            case 0b00: # ADD
                _output = Bit16((_input_A.unsigned + _input_B.unsigned) % (1 << 16))
                if VERBOSE_DEBUG: print(f"\talu.add({_input_A.unsigned}, {_input_B.unsigned}) = {_output.unsigned}\t@ {self}")
                return _output
            
            case 0b01: # AND
                _output = Bit16(_input_A.unsigned & _input_B.unsigned)
                if VERBOSE_DEBUG: print(f"\talu.and({_input_A.unsigned}, {_input_B.unsigned}) = {_output.unsigned}\t@ {self}")
                return _output
            
            case 0b10: # PASS
                _output = Bit16(_input_A.unsigned)
                if VERBOSE_DEBUG: print(f"\talu.pass({_input_A.unsigned}) = {_output.unsigned}\t@ {self}")
                return _output
            
            case 0b11: # NOT
                _output = Bit16(~ _input_A.unsigned)
                if VERBOSE_DEBUG: print(f"\talu.not({_input_A.unsigned}) = {_output.unsigned}\t@ {self}")
                return _output
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
            
    def zero_flag(self) -> Bit1:
        _input_A = self.input_A()
        _input_B = self.input_B()
        _output = Bit1(1) if _input_A.unsigned + _input_B.unsigned == 0 else Bit1(0)
        if VERBOSE_DEBUG: print(f"\talu.zero_flag({_input_A.unsigned}, {_input_B.unsigned}) = {_output.unsigned}\t@ {self}")
        return _output
    
    def negative_flag(self):    
        _input_A = self.input_A()
        _input_B = self.input_B()
        _output = Bit1(1) if _input_A.unsigned + _input_B.unsigned < 0 else Bit1(0)
        if VERBOSE_DEBUG: print(f"\talu.negative_flag({_input_A.unsigned}, {_input_B.unsigned}) = {_output.unsigned}\t@ {self}")
        return _output
    
def test():
    print("TEST 1: arithmetic logic unit")
    alu1 = ArithmeticLogicUnit()
    alu1.input_A = lambda: Bit16(8)
    alu1.input_B = lambda: Bit16(90)

    alu2 = ArithmeticLogicUnit()
    alu2.input_A = alu1.output
    alu2.input_B = lambda: Bit16(8)
    alu2.output()
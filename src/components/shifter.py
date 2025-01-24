from .bit_types import *

class Shifter():
    """
    amux = 0: A latch
    amux = 1: MBR
    """
    
    def opcode(self) -> Bit2:
        raise ConnectionError("Input unconnected")
    
    def input(self) -> Bit16:
        raise ConnectionError("Input unconnected")

    def output(self) -> Bit16:
        _input = self.input()
        _opcode = self.opcode()
        match(_opcode.unsigned):
            case 0b00: # NO SHIFT
                _output = Bit16(_input.unsigned)
                print()
                return _output
            
            case 0b01: # RIGHT SHIFT
                _output = Bit16(_input.unsigned >> 1)
                print()
                return _output
                        
            case 0b10:  # LEFT SHIFT
                _output = Bit16((_input.unsigned << 1) % (1 << 16))
                print()
                return _output
                                
            case 0b11: # NOT USED
                raise ArithmeticError("shifter opcode 3 does not exist")
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
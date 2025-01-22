from bit_types import *

class Shifter():
    """
    amux = 0: A latch
    amux = 1: MBR
    """
    def __init__(self):
        self.opcode : Bit2 = Bit2(0)
        self.input : Bit16 = Bit16(0)

    @property
    def output(self) -> Bit16:
        match(self.opcode.unsigned):
            case 0b00: # NO SHIFT
                return Bit16(self.input.unsigned)
            
            case 0b01: # RIGHT SHIFT
                return Bit16(self.input.unsigned >> 1)
                        
            case 0b10:  # LEFT SHIFT
                return Bit16((self.input.unsigned << 1) % (1 << 16))
                                
            case 0b11: # NOT USED
                raise ArithmeticError("shifter opcode 3 does not exist")
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")

"""
# TEST

shifter = Shifter()
shifter.opcode = Bit2(2) # left shift

shifter.input = Bit16(70)
print(shifter.output.unsigned)
print(shifter.output.signed)
# DEVE DAR x em um e -x no outro

shifter.input = Bit16(16384)
print(shifter.output.unsigned)
print(shifter.output.signed)
# DEVE DAR x em um e -x no outro

shifter.input = Bit16(32768)
print(shifter.output.unsigned)
print(shifter.output.signed)
# DEVE DAR 0 nos dois ou erro de range (mais provavel)
 """
from .bit_types import *

class Decoder4to16:
    def __init__(self):
        self.input : Bit4 = Bit4(0)

    @property
    def output(self) -> Bit16:
        return Bit16(1 << (self.input.unsigned))
    
""" 
# TEST
dec = Decoder4to16()
for i in range(16):
    dec.input = UInt4(i)
    print(f"---- {i} ----")
    print(bin(i))
    print(bin(dec.output.value)) """
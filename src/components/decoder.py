from .bit_types import *

class Decoder4to16:
    def __init__(self):
        self.input : UInt4 = UInt4(0)

    @property
    def output(self) -> UInt16:
        return UInt16(1 << (self.input.value))
    
""" 
# TEST
dec = Decoder4to16()
for i in range(16):
    dec.input = UInt4(i)
    print(f"---- {i} ----")
    print(bin(i))
    print(bin(dec.output.value)) """
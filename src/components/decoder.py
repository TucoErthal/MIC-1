from .bit_types import *

class Decoder4to16:
    def __init__(self):
        self.input : Bit4 = Bit4(0)

    @property
    def output(self) -> Bit16:
        _output = Bit16(1 << (self.input.unsigned))
        if VERBOSE_DEBUG: print(f"\tdecoder({self.input.unsigned}) = {_output.unsigned}")
        return _output
    
if TEST_COMPONENTS:
    dec = Decoder4to16()
    for i in range(16):
        dec.input = Bit4(i)
        print(f"---- {i} ----")
        print(f"0b{dec.output.unsigned:016b}")
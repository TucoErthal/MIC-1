from .bit_types import *

class Decoder4to16:
    def input(self) -> Bit4:
        raise ConnectionError("Input unconnected")
   
    def output(self) -> Bit16:
        _input = self.input()
        _output = Bit16(1 << (_input.unsigned))
        if VERBOSE_DEBUG: print(f"\tdecoder({_input.unsigned}) = {_output.unsigned}")
        return _output
    
def test():
    dec = Decoder4to16()
    for i in range(16):
        dec.input = lambda: Bit4(i)
        print(f"---- {i} ----")
        print(f"0b{dec.output().unsigned:016b}")
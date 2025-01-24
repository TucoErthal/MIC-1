from .bit_types import *

class Incrementer():
    def input(self) -> Bit8:
        raise ConnectionError("Input unconnected")
    
    def output(self) -> Bit8:
        _input = self.input()
        _output = Bit8(_input.unsigned + 1)
        if VERBOSE_DEBUG: print(f"\tincrementer({_input.unsigned}) = {_output.unsigned}")
        return _output # NAO ESTÁ DANDO OVERFLOW
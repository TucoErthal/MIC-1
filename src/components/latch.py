from .bit_types import *

class Latch[T: Bit]:
    def __init__(self, initial_value : T):
        self._value : T = initial_value

    def input(self) -> T:
        raise ConnectionError("Input unconnected")

    def write(self) -> Bit1:
        raise ConnectionError("Input unconnected")

    def output(self) -> T:
        _output = self._value
        if VERBOSE_DEBUG: print(f"\tregister.output() = {_output.unsigned}")
        return _output

    def update(self): # clock
        self._value = self.input() # PODE DAR MERDA AQUI COPIANDO POR REFERENCIA, NAO SEI
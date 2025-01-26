from .bit_types import *

class Register[T: Bit]:
    def __init__(self, initial_value : T, readonly : bool = False):
        self._value : T = initial_value
        self.readonly = readonly

    def input(self) -> T:
        raise ConnectionError("Input unconnected")

    def write(self) -> Bit1:
        raise ConnectionError("Input unconnected")

    def output(self) -> T:
        _output = self._value
        if VERBOSE_DEBUG: print(f"\tregister.output() = {_output.unsigned}")
        return _output

    def update(self): # clock
        _input = self.input()
        _write = self.write()
        if(self.readonly == False and _write.unsigned != 0):
            self._value = _input.copy()

def test():
    x = Register[Bit16](Bit16(0))
    x.input = lambda: Bit16(9)
    x.write = lambda: Bit1(1)
    x.update()
    x.output()
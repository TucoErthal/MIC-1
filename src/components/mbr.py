from .bit_types import *

class MemoryBufferRegister:
    def __init__(self):
        self._value : Bit16 = Bit16(0)
        self.data_bus : int #Bus16
    
    # CPU SIDE
    def input(self) -> Bit16: # DATA FROM SHIFTER
        raise ConnectionError("Input unconnected")
    
    def mbr(self) -> Bit1: # a.k.a. MBR bit da microinstrução, carrega o MBR com a saida do shifter
        raise ConnectionError("Input unconnected")
    
    def rd(self) -> Bit1:
        raise ConnectionError("Input unconnected")
    
    def wr(self) -> Bit1:
        raise ConnectionError("Input unconnected")

    def output(self) -> Bit16:
        _output = self._value
        if VERBOSE_DEBUG: print(f"\tregister.output() = {_output.unsigned}")
        return _output

    def update(self):
        _input = self.input()
        _mbr = self.mbr()
        _rd = self.rd()
        _wr = self.wr()
        
        if(_mbr.unsigned != 0): # LOADS MBR WITH DATA FROM SHIFTER
            self._value = _input.copy()

        if(_rd.unsigned != 0): # LOADS MBR WITH DATA FROM DATA BUS (takes 2 cycles to stabilize)
            self._value = self.data_bus.value()
        
        if(_wr.unsigned != 0): # WRITES INTERNAL DATA TO DATA BUS (takes 2 cycles for memory to store it)
            self.data_bus.write(self._value)

from .bit_types import *
from .mbr import *
import random

class Memory():
    def __init__(self):
        self.addr : Bit12 = Bit12(0)
        self.data : Bit12 = Bit12(0)
        self.bytes : list[Bit16] = [Bit16(random.randint(0, (1<<16)-1)) for _ in range(0, (1<<12))]
        
    def input_data(self) -> Bit16:
        raise ConnectionError("Input unconnected")
    
    #: MemoryBufferRegister = MemoryBufferRegister() # FROM / TO MBR

    def input_addr(self) -> Bit12: # FROM MAR
        raise ConnectionError("Input unconnected")

    def input_rd(self) -> Bit1:
        raise ConnectionError("Input unconnected")

    def input_wr(self) -> Bit1: 
        raise ConnectionError("Input unconnected")
    
    def output_data(self) -> Bit16:
        _input_addr = self.input_addr()
        _input_rd = self.input_rd()
        _output = self.bytes[_input_addr.unsigned]
        return _output


    def generate_garbage(self):
        self.bytes = [Bit16(random.randint(0, (1<<16)-1)) for _ in range(0, 16)]

    def update(self):
        _input_addr = self.input_addr()
        _input_rd = self.input_rd()
        _input_wr = self.input_wr()
        if _input_rd:
            pass
            #self.mbr.in self.bytes[_input_addr]
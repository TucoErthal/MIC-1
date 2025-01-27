from .bit_types import *
from .mbr import *
import random

class Memory():
    def __init__(self):
        self.bytes : list[Bit8] = [Bit8(random.randint(0, (1<<8)-1)) for _ in range(0, (1<<12))]
        self.mbr : MemoryBufferRegister = MemoryBufferRegister() # FROM / TO MBR

    def input_addr(self) -> Bit12:
        raise ConnectionError("Input unconnected")

    def input_rd(self) -> Bit1:
        raise ConnectionError("Input unconnected")

    def input_wr(self) -> Bit1: 
        raise ConnectionError("Input unconnected")

    def generate_garbage(self):
        self.bytes = [Bit8(random.randint(0, (1<<8)-1)) for _ in range(0, 16)]

    def update(self):
        _input_addr = self.input_addr()
        _input_rd = self.input_rd()
        _input_wr = self.input_wr()
        if _input_rd:
            self.mbr.in self.bytes[_input_addr]
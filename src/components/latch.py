from .bit_types import *
from .register import *

class Latch16(Register16):
    def __init__(self, output : Bit16 = Bit16(0), readonly : bool = False):
        super().__init__()
        self.write : Bit1 = Bit1(0)

    def update(self): # clock
        if(self.readonly == False and self.write._value != 0):
            self.output._value = self.input._value

class Register32:
    def __init__(self, output : Bit32 | Bit32 = Bit32(0), readonly : bool = False):
        self.input : Bit32 | Bit32 = Bit32(0)
        self.output = output
        self.write : Bit1 = Bit1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write._value != 0):
            if type(self.input) is not type(self.output):
                raise TypeError("Type mismatch: input and output must be of the same type.")
            self.output._value = self.input._value
from .bit_types import *
from .register import *

class Latch16(Register16):
    def __init__(self, output : Int16 = Int16(0), readonly : bool = False):
        super().__init__()
        self.write : UInt1 = UInt1(0)

    def update(self): # clock
        if(self.readonly == False and self.write.value != 0):
            self.output.value = self.input.value

class Register32:
    def __init__(self, output : Int32 | UInt32 = Int32(0), readonly : bool = False):
        self.input : Int32 | UInt32 = Int32(0)
        self.output = output
        self.write : UInt1 = UInt1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write.value != 0):
            if type(self.input) is not type(self.output):
                raise TypeError("Type mismatch: input and output must be of the same type.")
            self.output.value = self.input.value
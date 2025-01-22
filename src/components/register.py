from .bit_types import *

class Register8:
    def __init__(self, initial_value : Bit8 = Bit8(0), readonly : bool = False):
        self.input : Bit8 = Bit8(0)
        self.output : Bit8 = initial_value
        self.write : Bit1 = Bit1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write.unsigned != 0):
            self.output = Bit8(self.input.unsigned)

class Register12:
    def __init__(self, initial_value : Bit12 = Bit12(0), readonly : bool = False):
        self.input : Bit12 = Bit12(0)
        self.output : Bit12 = initial_value
        self.write : Bit1 = Bit1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write.unsigned != 0):
            self.output = Bit12(self.input.unsigned)

class Register16:
    def __init__(self, initial_value : Bit16 = Bit16(0), readonly : bool = False):
        self.input : Bit16 = Bit16(0)
        self._value : Bit16 = initial_value
        self.write : Bit1 = Bit1(0)
        self.readonly = readonly

    @property
    def output(self) -> Bit16:
        return Bit16(self._value.unsigned)

    def update(self): # clock
        if(self.readonly == False and self.write.unsigned != 0):
            self._value = Bit16(self.input.unsigned)

class Register32:
    def __init__(self, initial_value : Bit32 = Bit32(0), readonly : bool = False):
        self.input : Bit32 = Bit32(0)
        self.output : Bit32 = initial_value
        self.write : Bit1 = Bit1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write.unsigned != 0):
            self.output = Bit32(self.input.unsigned)
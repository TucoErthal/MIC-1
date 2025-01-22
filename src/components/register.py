from .bit_types import *

class Register8:
    def __init__(self, initial_value : Bit8 = Bit8(0), readonly : bool = False):
        self.input : Bit8 = Bit8(0)
        self.output = initial_value
        self.write : Bit1 = Bit1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write._value != 0):
            if type(self.input) is not type(self.output):
                raise TypeError("Type mismatch: input and output must be of the same type.")
            self.output._value = self.input._value

class Register12:
    def __init__(self, initial_value : Bit12 | Bit12 = Bit12(0), readonly : bool = False):
        self.input : Bit12 | Bit12 = Bit12(0)
        self.output = initial_value
        self.write : Bit1 = Bit1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write._value != 0):
            if type(self.input) is not type(self.output):
                raise TypeError("Type mismatch: input and output must be of the same type.")
            self.output._value = self.input._value

class Register16:
    def __init__(self, initial_value : Bit16 | Bit16 = Bit16(0), readonly : bool = False):
        self.input : Bit16 | Bit16 = Bit16(0)
        self.output = initial_value
        self.write : Bit1 = Bit1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write._value != 0):
            if type(self.input) is not type(self.output):
                raise TypeError("Type mismatch: input and output must be of the same type.")
            self.output._value = self.input._value

class Register32:
    def __init__(self, initial_value : Bit32 | Bit32 = Bit32(0), readonly : bool = False):
        self.input : Bit32 | Bit32 = Bit32(0)
        self.output = initial_value
        self.write : Bit1 = Bit1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write._value != 0):
            if type(self.input) is not type(self.output):
                raise TypeError("Type mismatch: input and output must be of the same type.")
            self.output._value = self.input._value


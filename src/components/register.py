from .bit_types import *

class Register12:
    def __init__(self, initial_value : Int12 | UInt12 = Int12(0), readonly : bool = False):
        self.input : Int12 | UInt12 = Int12(0)
        self.output = initial_value
        self.write : UInt1 = UInt1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write.value != 0):
            if type(self.input) is not type(self.output):
                raise TypeError("Type mismatch: input and output must be of the same type.")
            self.output.value = self.input.value

class Register16:
    def __init__(self, initial_value : Int16 | UInt16 = Int16(0), readonly : bool = False):
        self.input : Int16 | UInt16 = Int16(0)
        self.output = initial_value
        self.write : UInt1 = UInt1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write.value != 0):
            if type(self.input) is not type(self.output):
                raise TypeError("Type mismatch: input and output must be of the same type.")
            self.output.value = self.input.value

class Register32:
    def __init__(self, initial_value : Int32 | UInt32 = Int32(0), readonly : bool = False):
        self.input : Int32 | UInt32 = Int32(0)
        self.output = initial_value
        self.write : UInt1 = UInt1(0)
        self.readonly = readonly

    def update(self): # clock
        if(self.readonly == False and self.write.value != 0):
            if type(self.input) is not type(self.output):
                raise TypeError("Type mismatch: input and output must be of the same type.")
            self.output.value = self.input.value


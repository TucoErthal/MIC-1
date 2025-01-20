from .bit_types import *
from .register import *

class Scratchpad:
    def __init__(self):
        self.write : UInt1 = UInt1(0)

        # REGISTERS
        self.pc : Register16 = Register16()
        self.sp : Register16 = Register16()
        self.ir : Register16 = Register16()
        self.tir : Register16 = Register16() # temporary instruction register
        self.constant1 : Register16 = Register16()

""" 

        
    "0":        Register16(Int16(0), readonly = True),
    "+1":       Register16(Int16(1), readonly = True),
    "-1":       Register16(Int16(-1), readonly = True),
    "AMASK":    Register16(),
    "SMASK":    Register16(),
    "A":        Register16(),
    "B":        Register16(),
    "C":        Register16(),
    "D":        Register16(),
    "E":        Register16(),
    "F":        Register16()
} """

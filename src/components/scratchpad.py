from .bit_types import *
from .register import *

class Scratchpad:
    def __init__(self):
        self.write : UInt1 = UInt1(0)

        # CONSTANTS
        self.zero : Register16 = Register16(Int16(1), readonly = True)
        self.plus_one : Register16 = Register16(Int16(1), readonly = True)
        self.minus_one : Register16 = Register16(Int16(1), readonly = True)

        # REGISTERS
        self.pc : Register16 = Register16()
        self.sp : Register16 = Register16()
        self.ir : Register16 = Register16()
        self.tir : Register16 = Register16() # temporary instruction register
        self.amask : Register16 = Register16()
        self.smask : Register16 = Register16()
        self.a : Register16 = Register16()
        self.b : Register16 = Register16()
        self.c : Register16 = Register16()
        self.d : Register16 = Register16()
        self.e : Register16 = Register16()
        self.f : Register16 = Register16()

    def update(self):
        self.pc.update()
        self.sp.update()
        self.ir.update()
        self.tir.update()
        self.amask.update()
        self.smask.update()
        self.a.update()
        self.b.update()
        self.c.update()
        self.d.update()
        self.e.update()
        self.f.update()
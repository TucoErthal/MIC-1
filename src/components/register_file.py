from .bit_types import *
from .register import *

class RegisterFile:
    def __init__(self):
        self.input : Int16 | UInt16 = Int16(0)
        self.addr_A : UInt4 = UInt4(0)
        self.addr_B : UInt4 = UInt4(0)
        self.addr_C : UInt4 = UInt4(0)

        """
        C — selects register for storing into if ENC = 1: 0 = PC, 1 = AC, etc.
        B — selects B bus source: 0 = PC, 1 = AC, etc.
        A — selects A bus source: 0 = PC, 1 = AC, etc.
        """

        self.write : UInt1 = UInt1(0)

        self.registers = [
            Register16(),                               #pc
            Register16(),                               #sp
            Register16(),                               #ir
            Register16(),                               #tir
            Register16(Int16(1), readonly = True),      #zero
            Register16(Int16(1), readonly = True),      #plus_one
            Register16(Int16(1), readonly = True),      #minus_one
            Register16(),                               #amask
            Register16(),                               #smask
            Register16(),                               #a
            Register16(),                               #b
            Register16(),                               #c
            Register16(),                               #d
            Register16(),                               #e
            Register16()                                #f
        ]

        # C BUS
        for register in self.registers:
            register.input = self.input
            register.write = UInt1(1) # VEJA EXPLICAÇÃO ABAIXO
    
    @property
    def output_A(self) -> Int16 | UInt16:
        return self.registers[self.addr_A.value].output
    
    @property
    def output_B(self) -> Int16 | UInt16:
        return self.registers[self.addr_B.value].output

    def update(self):
        self.registers[self.addr_C.value].update()
        # o correto seria todos os registradores serem atualizados,
        # e só um ter o write ligado de cada vez, mas é mais facil
        # implementar assim do que usar writes separados e um mux








"""
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


# CONSTANTS
self.zero : Register16 = Register16(Int16(1), readonly = True)
self.plus_one : Register16 = Register16(Int16(1), readonly = True)
self.minus_one : Register16 = Register16(Int16(1), readonly = True)

# REGISTERS
self.pc : Register16 = Register16()
self.pc.input = self.input

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
"""
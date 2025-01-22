from .bit_types import *
from .register import *

class MicroinstructionRegister(Register32):
    def __init__(self):
        super().__init__(Bit32(0))
        self.write = Bit1(1)
    
    @property
    def addr(self)-> Bit8:
        return Bit8(bit_slice(self.input._value, 0, 8))
    
    @property
    def bus_A(self) -> Bit4:
        return Bit4(bit_slice(self.input._value, 8, 4))
    
    @property
    def bus_B(self) -> Bit4:
        return Bit4(bit_slice(self.input._value, 12, 4))
    
    @property
    def bus_C(self) -> Bit4:
        return Bit4(bit_slice(self.input._value, 16, 4))
    
    @property
    def encode_C(self) -> Bit1:
        return Bit1(bit_slice(self.input._value, 20, 1))
        
    @property
    def wr(self) -> Bit1:
        return Bit1(bit_slice(self.input._value, 21, 1))
    
    @property
    def rd(self) -> Bit1:
        return Bit1(bit_slice(self.input._value, 22, 1))
    
    @property
    def mar(self) -> Bit1:
        return Bit1(bit_slice(self.input._value, 23, 1))
    
    @property
    def mbr(self) -> Bit1:
        return Bit1(bit_slice(self.input._value, 24, 1))
    
    @property
    def shift(self)-> Bit2:
        return Bit2(bit_slice(self.input._value, 25, 2))
    
    @property
    def alu(self)-> Bit2:
        return Bit2(bit_slice(self.input._value, 27, 2))
    
    @property
    def cond(self) -> Bit2:
        """
        cond = 00: no branch
        cond = 01: branch if NEG
        cond = 10: branch if ZERO
        cond = 11: branch
        """
        return Bit2(bit_slice(self.input._value, 29, 2))
    
    @property
    def amux(self) -> Bit1:
        """
        amux = 0: A latch
        amux = 1: MBR
        """
        return Bit1(bit_slice(self.input._value, 31, 1))
    
    def debug(self):
        print("=====================")
        print(f"\nBYTE 0 = {bit_slice(self.input._value, 0, 8):08b}")
        print(f"\t(1) amux: {self.amux._value}")
        print(f"\t(2) cond: {self.cond._value}")
        print(f"\t(2) alu: {self.alu._value}")
        print(f"\t(2) shift: {self.shift._value}")
        print(f"\t(1) mbr: {self.mbr._value}")

        print(f"\nBYTE 1 = {bit_slice(self.input._value, 9, 8):08b}")
        print(f"\t(1) mar: {self.mar._value}")
        print(f"\t(1) rd: {self.rd._value}")
        print(f"\t(1) wr: {self.wr._value}")
        print(f"\t(1) encode_C: {self.encode_C._value}")
        print(f"\t(4) bus_C: {self.bus_C._value}")

        print(f"\nBYTE 2 = {bit_slice(self.input._value, 15, 8):08b}")
        print(f"\t(4) bus_B: {self.bus_B._value}")
        print(f"\t(4) bus_A: {self.bus_A._value}")

        print(f"\nBYTE 3 = {bit_slice(self.input._value, 25, 8):08b}")
        print(f"\t(8) addr: {self.addr._value}")
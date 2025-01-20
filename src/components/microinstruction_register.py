from .bit_types import *
from .register import *

class MicroinstructionRegister(Register32):
    def __init__(self):
        super().__init__(UInt32(0))
        self.write = UInt1(1)
    
    @property
    def addr(self)-> UInt8:
        return UInt8(bit_slice(self.input.value, 0, 8))
    
    @property
    def bus_A(self) -> UInt4:
        return UInt4(bit_slice(self.input.value, 8, 4))
    
    @property
    def bus_B(self) -> UInt4:
        return UInt4(bit_slice(self.input.value, 12, 4))
    
    @property
    def bus_C(self) -> UInt4:
        return UInt4(bit_slice(self.input.value, 16, 4))
    
    @property
    def encode_C(self) -> UInt1:
        return UInt1(bit_slice(self.input.value, 20, 1))
        
    @property
    def wr(self) -> UInt1:
        return UInt1(bit_slice(self.input.value, 21, 1))
    
    @property
    def rd(self) -> UInt1:
        return UInt1(bit_slice(self.input.value, 22, 1))
    
    @property
    def mar(self) -> UInt1:
        return UInt1(bit_slice(self.input.value, 23, 1))
    
    @property
    def mbr(self) -> UInt1:
        return UInt1(bit_slice(self.input.value, 24, 1))
    
    @property
    def shift(self)-> UInt2:
        return UInt2(bit_slice(self.input.value, 25, 2))
    
    @property
    def alu(self)-> UInt2:
        return UInt2(bit_slice(self.input.value, 27, 2))
    
    @property
    def cond(self) -> UInt2:
        """
        cond = 00: no branch
        cond = 01: branch if NEG
        cond = 10: branch if ZERO
        cond = 11: branch
        """
        return UInt2(bit_slice(self.input.value, 29, 2))
    
    @property
    def amux(self) -> UInt1:
        """
        amux = 0: A latch
        amux = 1: MBR
        """
        return UInt1(bit_slice(self.input.value, 31, 1))
    
    def debug(self):
        print("=====================")
        print(f"\nBYTE 0 = {bit_slice(self.input.value, 0, 8):08b}")
        print(f"\t(1) amux: {self.amux.value}")
        print(f"\t(2) cond: {self.cond.value}")
        print(f"\t(2) alu: {self.alu.value}")
        print(f"\t(2) shift: {self.shift.value}")
        print(f"\t(1) mbr: {self.mbr.value}")

        print(f"\nBYTE 1 = {bit_slice(self.input.value, 9, 8):08b}")
        print(f"\t(1) mar: {self.mar.value}")
        print(f"\t(1) rd: {self.rd.value}")
        print(f"\t(1) wr: {self.wr.value}")
        print(f"\t(1) encode_C: {self.encode_C.value}")
        print(f"\t(4) bus_C: {self.bus_C.value}")

        print(f"\nBYTE 2 = {bit_slice(self.input.value, 15, 8):08b}")
        print(f"\t(4) bus_B: {self.bus_B.value}")
        print(f"\t(4) bus_A: {self.bus_A.value}")

        print(f"\nBYTE 3 = {bit_slice(self.input.value, 25, 8):08b}")
        print(f"\t(8) addr: {self.addr.value}")
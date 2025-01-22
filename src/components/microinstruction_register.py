from .bit_types import *
from .register import *

class MicroinstructionRegister(Register32):
    def __init__(self):
        """
        
        AMUX = ?
        COND 10 (pulo incondicional)
        ALU = SOMA
        SH = no shift

        MBR
        MAR
        RD = 0
        WR = 0

        ENC = 1
        C = a
        B = b
        A = a
        ADDR = 0

            1   2   2   2   1   1   1   1   1   4       4       4       8
        0b  0   00  00  00  0   0   0   0   0   0000    0000    0000    00000000
        
            1   2   2   2   1   1   1   1   1   4       4       4       8
        0b  0   10  00  00  0   0   0   0   1   1001    1010    1001    00000001
                pi  sum n   ?   ?   0   0   en  a       b       a       0
        """
        super().__init__(Bit32(0))
        self.write = Bit1(1)
    
    @property
    def addr(self)-> Bit8:
        return Bit8(bit_slice(self.input.unsigned, 0, 8))
    
    @property
    def bus_A(self) -> Bit4:
        return Bit4(bit_slice(self.input.unsigned, 8, 4))
    
    @property
    def bus_B(self) -> Bit4:
        return Bit4(bit_slice(self.input.unsigned, 12, 4))
    
    @property
    def bus_C(self) -> Bit4:
        return Bit4(bit_slice(self.input.unsigned, 16, 4))
    
    @property
    def encode_C(self) -> Bit1:
        return Bit1(bit_slice(self.input.unsigned, 20, 1))
        
    @property
    def wr(self) -> Bit1:
        return Bit1(bit_slice(self.input.unsigned, 21, 1))
    
    @property
    def rd(self) -> Bit1:
        return Bit1(bit_slice(self.input.unsigned, 22, 1))
    
    @property
    def mar(self) -> Bit1:
        return Bit1(bit_slice(self.input.unsigned, 23, 1))
    
    @property
    def mbr(self) -> Bit1:
        return Bit1(bit_slice(self.input.unsigned, 24, 1))
    
    @property
    def shift(self)-> Bit2:
        return Bit2(bit_slice(self.input.unsigned, 25, 2))
    
    @property
    def alu(self)-> Bit2:
        return Bit2(bit_slice(self.input.unsigned, 27, 2))
    
    @property
    def cond(self) -> Bit2:
        """
        cond = 00: no branch
        cond = 01: branch if NEG
        cond = 10: branch if ZERO
        cond = 11: branch
        """
        return Bit2(bit_slice(self.input.unsigned, 29, 2))
    
    @property
    def amux(self) -> Bit1:
        """
        amux = 0: A latch
        amux = 1: MBR
        """
        return Bit1(bit_slice(self.input.unsigned, 31, 1))
    
    def debug(self):
        print("=====================")
        print(f"\nBYTE 0 = {bit_slice(self.input.unsigned, 0, 8):08b}")
        print(f"\t(1) amux: {self.amux.unsigned}")
        print(f"\t(2) cond: {self.cond.unsigned}")
        print(f"\t(2) alu: {self.alu.unsigned}")
        print(f"\t(2) shift: {self.shift.unsigned}")
        print(f"\t(1) mbr: {self.mbr.unsigned}")

        print(f"\nBYTE 1 = {bit_slice(self.input.unsigned, 9, 8):08b}")
        print(f"\t(1) mar: {self.mar.unsigned}")
        print(f"\t(1) rd: {self.rd.unsigned}")
        print(f"\t(1) wr: {self.wr.unsigned}")
        print(f"\t(1) encode_C: {self.encode_C.unsigned}")
        print(f"\t(4) bus_C: {self.bus_C.unsigned}")

        print(f"\nBYTE 2 = {bit_slice(self.input.unsigned, 15, 8):08b}")
        print(f"\t(4) bus_B: {self.bus_B.unsigned}")
        print(f"\t(4) bus_A: {self.bus_A.unsigned}")

        print(f"\nBYTE 3 = {bit_slice(self.input.unsigned, 25, 8):08b}")
        print(f"\t(8) addr: {self.addr.unsigned}")
from .bit_types import *
from .latch import *
from .microassembler import *

class MicroinstructionRegister(Latch[Bit32]):
    def __init__(self,
    _amux : int = 0, _cond : int = 0, _alu : int = 0, _sh : int = 0,
    _mbr : int = 0, _mar : int = 0, _rd : int = 0, _wr : int = 0, _enc : int = 0,
    _c : int = 0, _b : int = 0, _a : int = 0, _addr : int = 0):
        
        self._value = assemble_microinstruction(
            amux = _amux, cond = _cond, alu = _alu, sh = _sh,
            mbr = _mbr, mar = _mar, rd = _rd, wr = _wr, enc = _enc,
            c = _c, b = _b, a = _a, addr = _addr
        )
        
    def addr(self)-> Bit8:
        _input = self.input()
        _output = Bit8(bit_slice(_input.unsigned, 0, 8))
        return _output
    
    def a(self) -> Bit4:
        _input = self.input()
        _output = Bit4(bit_slice(_input.unsigned, 8, 4))
        return _output
    
    def b(self) -> Bit4:
        _input = self.input()
        _output = Bit4(bit_slice(_input.unsigned, 12, 4))
        return _output
    
    def c(self) -> Bit4:
        _input = self.input()
        _output = Bit4(bit_slice(_input.unsigned, 16, 4))
        return _output
    
    def enc(self) -> Bit1:
        _input = self.input()
        _output = Bit1(bit_slice(_input.unsigned, 20, 1))
        return _output
        
    def wr(self) -> Bit1:
        _input = self.input()
        _output = Bit1(bit_slice(_input.unsigned, 21, 1))
        return _output
    
    def rd(self) -> Bit1:
        _input = self.input()
        _output = Bit1(bit_slice(_input.unsigned, 22, 1))
        return _output
    
    def mar(self) -> Bit1:
        _input = self.input()
        _output = Bit1(bit_slice(_input.unsigned, 23, 1))
        return _output
    
    def mbr(self) -> Bit1:
        _input = self.input()
        _output = Bit1(bit_slice(_input.unsigned, 24, 1))
        return _output
    
    def sh(self)-> Bit2:
        _input = self.input()
        _output = Bit2(bit_slice(_input.unsigned, 25, 2))
        return _output
    
    def alu(self)-> Bit2:
        _input = self.input()
        _output = Bit2(bit_slice(_input.unsigned, 27, 2))
        return _output
    
    def cond(self) -> Bit2:
        """
        cond = 00: no branch
        cond = 01: branch if NEG
        cond = 10: branch if ZERO
        cond = 11: branch
        """
        _input = self.input()
        _output = Bit2(bit_slice(_input.unsigned, 29, 2))
        return _output
    
    def amux(self) -> Bit1:
        """
        amux = 0: A latch
        amux = 1: MBR
        """
        _input = self.input()
        _output = Bit1(bit_slice(_input.unsigned, 31, 1))
        return _output
    
    def debug(self):
        print("=====================")
        print(f"\nBYTE 0 = {bit_slice(self.input().unsigned, 24, 8):08b}")
        print(f"\t(1) amux: {self.amux().unsigned}")
        print(f"\t(2) cond: {self.cond().unsigned}")
        print(f"\t(2) alu: {self.alu().unsigned}")
        print(f"\t(2) shift: {self.sh().unsigned}")
        print(f"\t(1) mbr: {self.mbr().unsigned}")

        print(f"\nBYTE 1 = {bit_slice(self.input().unsigned, 16, 8):08b}")
        print(f"\t(1) mar: {self.mar().unsigned}")
        print(f"\t(1) rd: {self.rd().unsigned}")
        print(f"\t(1) wr: {self.wr().unsigned}")
        print(f"\t(1) encode_C: {self.enc().unsigned}")
        print(f"\t(4) bus_C: {self.c().unsigned}")

        print(f"\nBYTE 2 = {bit_slice(self.input().unsigned, 8, 8):08b}")
        print(f"\t(4) bus_B: {self.b().unsigned}")
        print(f"\t(4) bus_A: {self.a().unsigned}")

        print(f"\nBYTE 3 = {bit_slice(self.input().unsigned, 0, 8):08b}")
        print(f"\t(8) addr: {self.addr().unsigned}")
 
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
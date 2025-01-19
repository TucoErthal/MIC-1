from .bit_types import *

#                    TESTE NA MÃO
#                    0b 0000 0000 0000 0000 barB barA ADDR-----
#                    0b 0000 0000 0000 0000 10   5    128  7
#                    0b 0000 0000 0000 0000 1010 0101 1000 0111

def bit_slice(value : int, offset : int, width : int,):
    mask = (1 << width) - 1
    return (value >> offset) & mask

class MicroinstructionRegister():
    def __init__(self):
        self.microinstruction : UInt32 = UInt32(0)
    
    @property
    def addr(self):
        return bit_slice(self.microinstruction.value, 0, 8)
    
    @property
    def bus_A(self):
        return bit_slice(self.microinstruction.value, 8, 4)
    
    @property
    def bus_B(self):
        return bit_slice(self.microinstruction.value, 12, 4)
    
    @property
    def bus_C(self):
        return bit_slice(self.microinstruction.value, 16, 4)
    
    @property
    def en_C(self):
        return bit_slice(self.microinstruction.value, 20, 1)
        
    @property
    def WR(self):
        return bit_slice(self.microinstruction.value, 21, 1)
    
    @property
    def RD(self):
        return bit_slice(self.microinstruction.value, 22, 1)
    
    @property
    def MAR(self):
        return bit_slice(self.microinstruction.value, 23, 1)
    
    @property
    def MBR(self):
        return bit_slice(self.microinstruction.value, 24, 1)
    
    @property
    def DESL(self):
        return bit_slice(self.microinstruction.value, 25, 2)
    
    @property
    def ULA(self):
        return bit_slice(self.microinstruction.value, 27, 2)
    
    @property
    def COND(self):
        return bit_slice(self.microinstruction.value, 29, 2)
    
    @property
    def AMux(self):
        return bit_slice(self.microinstruction.value, 31, 1)
    
    
"""
# ================ TESTS ====================
obj = MicroinstructionRegister()
obj.original_value = 0b00000000000000001010010110000111
print(f"Original Value: {obj.original_value}")
print(f"addr: {obj.addr: 08b}")
print(f"barr_A: {obj.barr_A: 04b}")
print(f"barr_B: {obj.barr_B: 04b}")
print(f"barr_C: {obj.barr_C: 04b}")

print(f"original: {0b110010}, masked = {bitmask(0b110010, 5, 1)}") """
from bit_types import *
from bitstring import BitArray

class Shifter():
    """
    amux = 0: A latch
    amux = 1: MBR
    """
    def __init__(self):
        self.opcode : UInt2 = UInt2(0)
        self.input : Int16 = Int16(0)

    @property
    def output(self) -> Int16:
        match(self.opcode.value):
            case 0b00: # NO SHIFT
                return Int16(self.input.value)
            
            case 0b01: # RIGHT SHIFT
                return Int16(self.input.value >> 1)
            
            case 0b10:  # LEFT SHIFT
                return BitArray(bin='1111111111111010').
            
            ba2int((int2ba(value, length=16, signed=True) << 1)[-16:], signed=True)
                
            case 0b11: # NOT USED
                raise ValueError("shifter opcode 3 does not exist")
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
            
""" # TEST
shifter = Shifter()
shifter.opcode = UInt2(2)
shifter.input = Int16(32767) # o primeiro bit é 0, dps é tudo 1. o original é pra ser um numero grande
print(shifter.output)
print(shifter.output.value) """

print((16384)<<1) # TEM QUE DAR -1


"""
o range é de
-(2^15) = -32768
até
(2^15)-1 = 32767

MSB vale -(2^15) = -32768
o prox vale 2^14 = 16384

numeros com o MSB = 0 são positivos. Se o prox for 1, eles tão entre 16384 e 32767 (maximo)
NESSE CASO os numeros vao ficar negativos





               -1__________________
32767      = 0b 0111 1111 1111 1111
32767 << 1 = 0b 1111 1111 1111 1110 = 2

"""
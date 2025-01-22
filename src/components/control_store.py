from .bit_types import *

class ControlStore:
    def __init__(self):
        self.microprogram : list[Bit32] = [ # 256 microinstructions, log(256) MPC
            
            #AMUX=1, COND=0, ALU=0, SH=0, MBR/MAR/RD/WR=0, ENC=1, C=9, B=5, A=4, ADDR=1
            Bit32(0b10000000000110010110010000000001)

            #AMUX=1, COND=0, ALU=0, SH=0, MBR/MAR/RD/WR=1, C=9, B=0, A=0, ADDR=1
        ]
        self.mpc : Bit8 = Bit8(0)

    @property
    def output(self) -> Bit32:
        _output = self.microprogram[self.mpc.unsigned]
        if VERBOSE_DEBUG: print(f"\tcs({self.mpc.unsigned}) = {_output.unsigned:08x}")
        return _output
    
    
def test():
    print("TEST 2: control_store")
    cs = ControlStore()
    cs.microprogram = [Bit32(0xfeedbeef)]
    cs.output
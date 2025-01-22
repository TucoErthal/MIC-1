from .bit_types import *

class ControlStore:
    def __init__(self):
        self.microprogram : list[Bit32] = [ # 256 microinstructions, log(256) MPC
            Bit32(0b0),
            Bit32(0xaffffffa)
        ]
        self.mpc : Bit8 = Bit8(0)

    @property
    def output(self) -> Bit32:
        return self.microprogram[self.mpc._value]
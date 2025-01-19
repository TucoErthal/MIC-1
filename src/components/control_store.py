from .bit_types import *

class ControlStore:
    def __init__(self):
        self.microprogram : list[UInt32] = [ # 256 microinstructions, log(256) MPC´
            UInt32(0b0),
            UInt32(0xaffffffa)
        ]
        self.mpc : UInt8 = UInt8(0)

    @property
    def output(self) -> UInt32:
        return self.microprogram[self.mpc.value]
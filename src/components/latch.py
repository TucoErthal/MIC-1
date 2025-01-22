from .bit_types import *
from .register import *

class Latch16(Register16):
    def __init__(self, output : Bit16 = Bit16(0), readonly : bool = False):
        super().__init__()
        self.write : Bit1 = Bit1(0)
from .bit_types import *

class Incrementer():
    def __init__(self):
        self.input : Bit8 = Bit8(0)

    @property
    def output(self):
        return Bit8(self.input.unsigned + 1) # NAO ESTÁ DANDO OVERFLOW
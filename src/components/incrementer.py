from .bit_types import *

class Incrementer():
    def __init__(self):
        self.input : UInt8 = UInt8(0)

    @property
    def output(self):
        return UInt8(self.input.value + 1) # NAO ESTÁ DANDO OVERFLOW
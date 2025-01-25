from .bit_types import *

class Multiplexer16by2:
    def input_A(self) -> Bit16:
        raise ConnectionError("Input unconnected")

    def input_B(self) -> Bit16:
        raise ConnectionError("Input unconnected")

    def select(self) -> Bit1:
        raise ConnectionError("Input unconnected")

    def output(self) -> Bit16:
        _select = self.select()
        match(_select.unsigned):
            case 0:
                return self.input_A()
            
            case 1: 
                return self.input_B()
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
            
class Multiplexer8by2:
    def input_A(self) -> Bit8:
        raise ConnectionError("Input unconnected")

    def input_B(self) -> Bit8:
        raise ConnectionError("Input unconnected")

    def select(self) -> Bit1:
        raise ConnectionError("Input unconnected")

    def output(self) -> Bit8:        
        _select = self.select()
        match(_select.unsigned):
            case 0:
                return self.input_A()
            
            case 1: 
                return self.input_B()
            
            case _:    # IMPOSSIBLE
                raise ValueError("huh?")
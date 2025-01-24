from .bit_types import *
from .register import *

class RegisterFile:
    
    def input_data(self) -> Bit16:
        raise ConnectionError("Data Input unconnected")

    def input_addr_A(self) -> Bit4:
        raise ConnectionError("Input unconnected")

    def input_addr_B(self) -> Bit4:
        raise ConnectionError("Input unconnected")

    def input_addr_C(self) -> Bit4:
        raise ConnectionError("Input unconnected")

    def __init__(self):
        """
        C — selects register for storing into if ENC = 1: 0 = PC, 1 = AC, etc.
        B — selects B bus source: 0 = PC, 1 = AC, etc.
        A — selects A bus source: 0 = PC, 1 = AC, etc.
        """

        self.write : Bit1 = Bit1(0)

        self.registers : dict[str, Register[Bit16]] = {
            "pc":           Register[Bit16](Bit16(0)),                               
            "sp":           Register[Bit16](Bit16(0)),                               
            "ir":           Register[Bit16](Bit16(0)),                               
            "tir":          Register[Bit16](Bit16(0)),                               
            "zero":         Register[Bit16](Bit16(0), readonly = True),      
            "plus_one":     Register[Bit16](Bit16(1), readonly = True),      
            "minus_one":    Register[Bit16](Bit16((1<<16)-1), readonly = True),      
            "amask":        Register[Bit16](Bit16(0)),                               
            "smask":        Register[Bit16](Bit16(0)),                               
            "a":            Register[Bit16](Bit16(9)),                               
            "b":            Register[Bit16](Bit16(2)),                               
            "c":            Register[Bit16](Bit16(0)),                               
            "d":            Register[Bit16](Bit16(0)),                               
            "e":            Register[Bit16](Bit16(0)),                               
            "f":            Register[Bit16](Bit16(0))                                
        }

    def setup(self):
        for register in self.registers.values():
            register.input = self.input_data
            register.write = lambda: Bit1(1) # VEJA EXPLICAÇÃO ABAIXO

    
    def output_A(self) -> Bit16:
        _keys = list(self.registers.keys())
        _input_addr_A = self.input_addr_A()
        _output = self.registers[_keys[_input_addr_A.unsigned]].output()
        return _output
    
    def output_B(self) -> Bit16:
        _keys = list(self.registers.keys())
        _input_addr_B = self.input_addr_B()
        _output = self.registers[_keys[_input_addr_B.unsigned]].output()
        return _output

    def update(self):
        _keys = list(self.registers.keys())
        _input_addr_C = self.input_addr_C()
        self.registers[_keys[_input_addr_C.unsigned]].update()
        # o correto seria todos os registradores serem atualizados,
        # e só um ter o write ligado de cada vez, mas é mais facil
        # implementar assim do que usar writes separados e um mux
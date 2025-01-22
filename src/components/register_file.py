from .bit_types import *
from .register import *

class RegisterFile:
    def __init__(self):
        self.input : Bit16 = Bit16(0)
        self.addr_A : Bit4 = Bit4(0)
        self.addr_B : Bit4 = Bit4(0)
        self.addr_C : Bit4 = Bit4(0)

        """
        C — selects register for storing into if ENC = 1: 0 = PC, 1 = AC, etc.
        B — selects B bus source: 0 = PC, 1 = AC, etc.
        A — selects A bus source: 0 = PC, 1 = AC, etc.
        """

        self.write : Bit1 = Bit1(0)

        self.registers : dict[str, Register16] = {
            "pc":           Register16(),                               
            "sp":           Register16(),                               
            "ir":           Register16(),                               
            "tir":          Register16(),                               
            "zero":         Register16(Bit16(0), readonly = True),      
            "plus_one":     Register16(Bit16(1), readonly = True),      
            "minus_one":    Register16(Bit16((1<<16)-1), readonly = True),      
            "amask":        Register16(),                               
            "smask":        Register16(),                               
            "a":            Register16(Bit16(9)),                               
            "b":            Register16(Bit16(2)),                               
            "c":            Register16(),                               
            "d":            Register16(),                               
            "e":            Register16(),                               
            "f":            Register16()                                
        }

        # C BUS
        for register in self.registers.values():
            register.input = self.input
            register.write = Bit1(1) # VEJA EXPLICAÇÃO ABAIXO

    def reset(self):
        self.registers : dict[str, Register16] = {
            "pc":           Register16(),                               
            "sp":           Register16(),                               
            "ir":           Register16(),                               
            "tir":          Register16(),                               
            "zero":         Register16(Bit16(0), readonly = True),      
            "plus_one":     Register16(Bit16(1), readonly = True),      
            "minus_one":    Register16(Bit16((1<<16)-1), readonly = True),      
            "amask":        Register16(),                               
            "smask":        Register16(),                               
            "a":            Register16(Bit16(9)),                               
            "b":            Register16(Bit16(2)),                               
            "c":            Register16(),                               
            "d":            Register16(),                               
            "e":            Register16(),                               
            "f":            Register16()                                
        }
    
    @property
    def output_A(self) -> Bit16:
        keys = list(self.registers.keys())
        return self.registers[keys[self.addr_A.unsigned]].output
    
    @property
    def output_B(self) -> Bit16:
        keys = list(self.registers.keys())
        return Bit16(self.registers[keys[self.addr_B.unsigned]].output.unsigned)

    def update(self):
        keys = list(self.registers.keys())
        self.registers[keys[self.addr_C.unsigned]].update()
        # o correto seria todos os registradores serem atualizados,
        # e só um ter o write ligado de cada vez, mas é mais facil
        # implementar assim do que usar writes separados e um mux
from .bit_types import *
import random

class Memory():
    def __init__(self):
        self.bytes : list[Bit8] = [Bit8(random.randint(0, (1<<8)-1)) for _ in range(0, 16)]
        self.addr : Bit12 = Bit12(0)
        self.data : Bit12 = Bit12(0)

    def generate_garbage(self):
        self.bytes = [Bit8(random.randint(0, (1<<8)-1)) for _ in range(0, 16)]

    def update(self):
        pass
        #self.bytes[self.addr.unsigned].update()
        # o correto seria todos os registradores serem atualizados,
        # e só um ter o write ligado de cada vez, mas é mais facil
        # implementar assim do que usar writes separados e um mux
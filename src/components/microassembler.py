from .bit_types import *
from typing import BinaryIO

def assemble_microinstruction(
amux : int = 0, cond : int = 0, alu : int = 0, sh : int = 0,
mbr : int = 0, mar : int = 0, rd : int = 0, wr : int = 0, enc : int = 0,
c : int = 0, b : int = 0, a : int = 0, addr : int = 0):

    return Bit32(
        (Bit1(amux).unsigned << 31) + (Bit2(cond).unsigned << 29) + (Bit2(alu).unsigned << 27) + (Bit2(sh).unsigned << 25) +
        (Bit1(mbr).unsigned << 24) + (Bit1(mar).unsigned << 23) + (Bit1(rd).unsigned << 22) + (Bit1(wr).unsigned << 21) + (Bit1(enc).unsigned << 20) + 
        (Bit4(c).unsigned << 16) + (Bit4(b).unsigned << 12) + (Bit4(a).unsigned << 8) + (Bit8(addr).unsigned)
    )

def assemble_microprogram(filename : str, microprogram : list[Bit32]):
    file = open(filename, "wb+")
    for i in microprogram:
        file.write(i.unsigned.to_bytes(4, "big"))
    return file

def deserialize(stream : BinaryIO) -> list[Bit32]:
    microprogram : list[Bit32] = []
    while True:
        bytes = stream.read(4)
        if not(bytes): break
        microprogram.append(Bit32(int.from_bytes(bytes, "big")))
    return microprogram

def deserialize_file(filename : str) -> list[Bit32]:
    microprogram : list[Bit32] = []
    file = open(filename, "rb")
    while True:
        bytes = file.read(4)
        if not(bytes): break
        microprogram.append(Bit32(int.from_bytes(bytes, "big")))

    return microprogram
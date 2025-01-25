from .bit_types import *

def serialize(filename : str, microprogram : list[Bit32]):
    file = open(filename, "wb+")
    for i in microprogram:
        file.write(i.unsigned.to_bytes(4, "big"))
    return file

def deserialize(filename : str) -> list[Bit32]:
    microprogram : list[Bit32] = []
    file = open(filename, "rb")
    while True:
        bytes = file.read(4)
        if not(bytes): break
        microprogram.append(Bit32(int.from_bytes(bytes, "big")))

    return microprogram
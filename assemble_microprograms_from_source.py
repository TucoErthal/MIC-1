from src.components.microassembler import * 

assemble_microprogram("microprograms/counter.mic1", [
    assemble_microinstruction(),
    assemble_microinstruction(enc=1, c=9, b=5, a=4),                     # load 1 into "a"
    assemble_microinstruction(cond=3, enc=1, c=9, b=5, a=9, addr=2),     # while(true): "a" += 1
])

assemble_microprogram("microprograms/fibonacci.mic1", [
    assemble_microinstruction(),

    assemble_microinstruction(enc=1, c=9, a=5, alu=2),
    assemble_microinstruction(enc=1, c=10, a=5, alu=2),

    assemble_microinstruction(enc=1, c=9, a=10, b=9),
    assemble_microinstruction(enc=1, c=10, a=9, b=10, cond=3, addr=3),
])
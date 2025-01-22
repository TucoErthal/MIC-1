from components import *

alu = ArithmeticLogicUnit()
alu.opcode = Bit2(0)

alu.input_A = Bit16(65535)
alu.input_B = Bit16(1)
print(alu.output.unsigned)
print(alu.output.signed)
from components import *

""" alu = ArithmeticLogicUnit()
alu.opcode = Bit2(0)

alu.input_A = Bit16(65535)
alu.input_B = Bit16(1)
print(alu.output.unsigned)
print(alu.output.signed)

 """

output = Bit16(69)

latch_A = Latch16()
latch_B = Latch16()


latch_A.input = output

print(latch_A.output.unsigned)

latch_A.update()
print(latch_A.output.unsigned)
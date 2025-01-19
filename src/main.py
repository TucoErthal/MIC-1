from nicegui import ui
from components import *

# ====================== DATAPATH ======================

alu = ArithmeticLogicUnit()
mir = MicroinstructionRegister()

register_file : dict[str, Register16] = {

    "PC":       Register16(),
    "SP":       Register16(),
    "IR":       Register16(),
    "TIR":      Register16(),
    "0":        Register16(Int16(0), readonly = True),
    "+1":       Register16(Int16(1), readonly = True),
    "-1":       Register16(Int16(-1), readonly = True),
    "AMASK":    Register16(),
    "SMASK":    Register16(),
    "A":        Register16(),
    "B":        Register16(),
    "C":        Register16(),
    "D":        Register16(),
    "E":        Register16(),
    "F":        Register16()
}

# ====================== USER INTERFACE ======================

def throw_error(message: str):
    ui.notify(message, color="red")

button = ui.button("throw error", on_click = lambda: throw_error("core dumped"))

ui.toggle(["MAC-1", "MIC-1"])
    
ui.run(port=8080)

""" reg1 = components.Register(width = 8) # cria um registrador de 8 bits
reg1.write.overwrite(BitArray(uint = 1, length = 1), 0) # write

reg1.input.overwrite(BitArray(uint = 255, length = 8), 0)
reg1.update()
print(reg1.output)

reg1.input.overwrite(BitArray(uint = 257, length = 9), 0)
reg1.update()
print(reg1.output)
 """
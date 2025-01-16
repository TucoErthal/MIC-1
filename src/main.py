from nicegui import ui
import components

# ====================== DATAPATH ======================

alu = components.ArithmeticLogicUnit()
#mir = components.MicroinstructionRegister()

# ====================== USER INTERFACE ======================

""" def throw_error(message: str):
    ui.notify(message, color="red")

button = ui.button("throw error", on_click = lambda: throw_error("core dumped"))

ui.toggle(["MAC-1", "MIC-1"])
    
ui.run(port=8080) """

import components
from bitstring import BitArray

reg1 = components.Register(width = 8) # cria um registrador de 8 bits
reg1.write.overwrite(BitArray(uint = 1, length = 1), 0) # write

reg1.input.overwrite(BitArray(uint = 255, length = 8), 0)
reg1.update()
print(reg1.output)

reg1.input.overwrite(BitArray(uint = 257, length = 9), 0)
reg1.update()
print(reg1.output)

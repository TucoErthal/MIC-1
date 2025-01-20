from nicegui import ui
from components import *

# ================================ DATAPATH ================================

memory = Memory()

latch_A = Register16()
latch_B = Register16()
alu = ArithmeticLogicUnit()

# ================================ CONTROL UNIT ================================

control_store : ControlStore = ControlStore()
control_store.mpc = UInt8(1)

mir = MicroinstructionRegister()
mir.input = control_store.output
mir.debug()

# ================================ CLOCK ================================

def subcycle1():
    mir.update()

def subcycle2():
    latch_A.update()
    latch_B.update()

def subcycle3():
    pass

def subcycle4():
    pass

def cycle():
    subcycle1()
    subcycle2()
    subcycle3()
    subcycle4()

scratchpad : Scratchpad

decoder_A = Decoder4to16()
decoder_A.input = mir.bus_A

decoder_B = Decoder4to16()
decoder_B.input = mir.bus_B

# ====================== USER INTERFACE ======================

def throw_error(message: str):
    ui.notify(message, color="red")

button = ui.button("throw error", on_click = lambda: throw_error("core dumped"))

ui.toggle(["MAC-1", "MIC-1"])
    
ui.run(port=8080)
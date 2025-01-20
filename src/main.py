from nicegui import ui
from components import *

# ================================ DATAPATH ================================

memory = Memory()



scratchpad : Scratchpad = Scratchpad()
latch_A = Register16()
latch_B = Register16()
#MAR(12 bits)
#MBR(12 bits)
#AMUX
alu = ArithmeticLogicUnit()
#shifter

# =================== BUSES

#A_BUS: SCRATCHPAD TO LATCH_A
#B_BUS: SCRATCHPAD TO LATCH_B
#A_LATCH TO AMUX
#B_LATCH TO ALU
#B_LATCH TO MBR
#MBR TO AMUX
#AMUX TO ALU
#ALU TO SHIFTER
#SHIFTER TO SCRATCHPAD

# ================================ CONTROL UNIT ================================

control_store : ControlStore = ControlStore()
control_store.mpc = UInt8(1)

mir = MicroinstructionRegister()
mir.input = control_store.output
mir.debug()


decoder_A = Decoder4to16()
decoder_A.input = mir.bus_A

decoder_B = Decoder4to16()
decoder_B.input = mir.bus_B

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

# ====================== USER INTERFACE ======================

def throw_error(message: str):
    ui.notify(message, color="red")

button = ui.button("throw error", on_click = lambda: throw_error("core dumped"))

ui.toggle(["MAC-1", "MIC-1"])
    
ui.run(port=8080)
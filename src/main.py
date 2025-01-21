from nicegui import ui
from components import *

# ================================ DATAPATH ================================

memory = Memory()

scratchpad : RegisterFile = RegisterFile()
latch_A = Register16()
latch_B = Register16()
mar = Register16() #MAR(12 bits)
mbr = Register16() #MBR(12 bits)
amux = Multiplexer16by2() #AMUX
alu = ArithmeticLogicUnit()
sh = Shifter() #shifter

# =================== BUSES

latch_A.input = scratchpad.output_A     #A_BUS: SCRATCHPAD TO LATCH_A
latch_B.input = scratchpad.output_B     #B_BUS: SCRATCHPAD TO LATCH_B

amux.input_B = latch_A.output           #A_LATCH TO AMUX
alu.input_B = latch_B.output            #B_LATCH TO ALU
mbr.input = latch_B.output              #B_LATCH TO MBR
amux.input_A = mbr.output               #MBR TO AMUX
alu.input_A = amux.output               #AMUX TO ALU
sh.input                                #ALU TO SHIFTER
scratchpad.input = sh.output            #SHIFTER TO SCRATCHPAD

# ================================ CONTROL UNIT ================================

cs : ControlStore = ControlStore()
cs.mpc = UInt8(1)

mir = MicroinstructionRegister()
mir.input = cs.output
mir.debug()


decoder_A = Decoder4to16()
decoder_A.input = mir.bus_A

decoder_B = Decoder4to16()
decoder_B.input = mir.bus_B

# ================================ CLOCK ================================

class Clock:
    def __init__(self):
        self.current_cycle = 1
        self.current_subcycle = 1

def subcycle1():
    mir.update()
    ui.notify("subcycle 1")

def subcycle2():
    latch_A.update()
    latch_B.update()
    ui.notify("subcycle 2")

def subcycle3():
    ui.notify("subcycle 3")

def subcycle4():
    ui.notify("subcycle 4")

def step_subcycle():
    match(clock.current_subcycle):
        case 1:
            subcycle1()
            clock.current_subcycle += 1
        case 2:
            subcycle2()
            clock.current_subcycle += 1
        case 3:
            subcycle3()
            clock.current_subcycle += 1
        case 4:
            subcycle4()
            clock.current_subcycle = 1
        case _: pass

def step_cycle():
    subcycle1()
    subcycle2()
    subcycle3()
    subcycle4()
    clock.current_cycle += 1

clock = Clock()

# ====================== USER INTERFACE ======================

def throw_error(message: str):
    ui.notify(message, color="red")

with ui.column():
    with ui.row():
        ui.label().bind_text_from(clock, "current_cycle")
        ui.toggle({1: '1', 2: '2', 3: '3', 4: '4'}).bind_value_from(clock, "current_subcycle")

    with ui.button_group():
        with ui.button(icon = "play_arrow", on_click = step_subcycle):
            ui.tooltip("Step subcycle")#.classes('bg-green')

        with ui.button(icon = "play_arrow", on_click = step_cycle):
            ui.tooltip("Step cycle")#.classes('bg-green')

        with ui.button(icon = "play_arrow"):
            ui.tooltip("Stop execution")#.classes('bg-green')
   
    
ui.run(port=8080)

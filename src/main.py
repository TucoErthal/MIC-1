from nicegui import ui
from components import *

# ================================ DATAPATH ================================

mem = Memory()

scratchpad : RegisterFile = RegisterFile()

latch_A = Register16()
latch_A.write = Bit1(1)
latch_B = Register16()
latch_B.write = Bit1(1)

mar = Register16() #MAR(12 bits)
mbr = Register16() #MBR(12 bits)
amux = Multiplexer16by2() #AMUX
alu = ArithmeticLogicUnit()
sh = Shifter() #shifter

# =================== BUSES

latch_A.input = scratchpad.output_A     #A_BUS: SCRATCHPAD TO LATCH_A
latch_B.input = scratchpad.output_B     #B_BUS: SCRATCHPAD TO LATCH_B

amux.input_B = latch_A.output           #A_LATCH TO AMUX
alu.input_B() = latch_B.output            #B_LATCH TO ALU
mbr.input = latch_B.output              #B_LATCH TO MBR
amux.input_A = mbr.output               #MBR TO AMUX
alu.input_A() = amux.output               #AMUX TO ALU
sh.input = alu.output                   #ALU TO SHIFTER
scratchpad.input_data = sh.output            #SHIFTER TO SCRATCHPAD

# ================================ CONTROL UNIT ================================

#decoder_A = Decoder4to16()
#decoder_B = Decoder4to16()
mmux = Multiplexer8by2()
inc = Incrementer()
mpc = Register8()
cs : ControlStore = ControlStore()
mir = MicroinstructionRegister()
ms = MicroSequencer()

# =================== BUSES

#decoder_A.input = mir.bus_A
#decoder_B.input = mir.bus_B
# DECODER C
mmux.input_A = inc.output
mmux.input_B = mir.addr
mmux.select = ms.output
inc.input = mpc.output
mpc.input = mmux.output
cs.input = mpc.output
mir.input = cs.output
ms.input_cond = mir.cond
ms.input_negative_flag = alu.negative_flag
ms.input_zero_flag = alu.zero_flag

# to datapath
scratchpad.input_addr_A = mir.bus_A
scratchpad.input_addr_B = mir.bus_B
scratchpad.input_addr_C = mir.bus_C

amux.select = mir.amux
alu.opcode = mir.alu
sh.opcode = mir.shift

def reset():
    mem.generate_garbage()
    scratchpad.reset()

    clock.current_cycle = 1
    clock.current_subcycle = 1

# ================================ CLOCK ================================

class Clock:
    def __init__(self):
        self.current_cycle = 1
        self.current_subcycle = 1

def subcycle1():
    mir.update()

def subcycle2():    
    """ print("scratchpad.addr_B", scratchpad.addr_B.unsigned)
    print("scratchpad.output_B", scratchpad.output_B.unsigned)
    print("latch_B.input", latch_B.input.unsigned)
    print("latch_B.output", latch_B.output.unsigned) """
    latch_B.update()
    print("latch_B.output", latch_B.output.unsigned)

    """  print("scratchpad.addr_B", scratchpad.addr_B.unsigned)
    print("scratchpad.output_B", scratchpad.output_B.unsigned)
    print("latch_B.input", latch_B.input.unsigned)
    print("latch_B.output", latch_B.output.unsigned) """
    print("latch_B.output", latch_B.output.unsigned)

def subcycle3():
    # MBR MAR

def subcycle4():    
    scratchpad.update()
    clock.current_cycle += 1

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
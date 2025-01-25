from components import *

# ================================ DATAPATH ================================

mem = Memory()

scratchpad : RegisterFile = RegisterFile()

latch_A = Latch[Bit16](Bit16(0))
latch_B = Latch[Bit16](Bit16(0))

mar = Register[Bit16](Bit16(0)) #MAR(12 bits)
mbr = Register[Bit16](Bit16(0)) #MBR(12 bits)
amux = Multiplexer16by2() #AMUX
alu = ArithmeticLogicUnit()
sh = Shifter() #shifter

# =================== BUSES

latch_A.input = scratchpad.output_A     #A_BUS: SCRATCHPAD TO LATCH_A
latch_B.input = scratchpad.output_B     #B_BUS: SCRATCHPAD TO LATCH_B

amux.input_A = latch_A.output           #A_LATCH TO AMUX
alu.input_B = latch_B.output            #B_LATCH TO ALU
mbr.input = latch_B.output              #B_LATCH TO MBR
amux.input_B = mbr.output               #MBR TO AMUX
alu.input_A = amux.output               #AMUX TO ALU
sh.input = alu.output                   #ALU TO SHIFTER
scratchpad.input_data = sh.output       #SHIFTER TO SCRATCHPAD
scratchpad.setup()
# ================================ CONTROL UNIT ================================

#decoder_A = Decoder4to16()
#decoder_B = Decoder4to16()
mmux = Multiplexer8by2()
inc = Incrementer()
mpc = Latch[Bit8](Bit8(0))
cs : ControlStore = ControlStore()
mir = MicroinstructionRegister()
ms = MicroSequencer()

# =================== BUSES

#decoder_A.input = mir.bus_A
#decoder_B.input = mir.bus_B
# DECODER C
mmux.input_A = mir.addr
mmux.input_B = inc.output
mmux.select = ms.output
inc.input = mpc.output
mpc.input = mmux.output
cs.input = mpc.output
mir.input = cs.output
ms.input_cond = mir.cond
ms.input_negative_flag = alu.negative_flag
ms.input_zero_flag = alu.zero_flag

# to datapath
scratchpad.input_addr_A = mir.a
scratchpad.input_addr_B = mir.b
scratchpad.input_addr_C = mir.c

amux.select = mir.amux
alu.opcode = mir.alu
sh.opcode = mir.sh

def reset():
    mem.generate_garbage()
    #scratchpad.reset()

    clock.current_cycle = 1
    clock.current_subcycle = 1

# ================================ CLOCK ================================

class Clock:
    def __init__(self):
        self.current_cycle = 1
        self.current_subcycle = 1

def subcycle1():
    mir.update()
    clock.current_cycle += 1

def subcycle2():    
    latch_A.update()
    latch_B.update()
    clock.current_cycle += 1
    
def subcycle3():
    # MAR update
    clock.current_cycle += 1

def subcycle4():
    mpc.update()    
    # C DECODER, oficialmente (mas acho que n precisa)
    scratchpad.update()
    # MBR

    clock.current_cycle += 1

def step_subcycle():
    match(clock.current_subcycle):
        case 1:
            subcycle1()
        case 2:
            subcycle2()
        case 3:
            subcycle3()
        case 4:
            subcycle4()
        case _: pass

def step_cycle():
    subcycle1()
    subcycle2()
    subcycle3()
    subcycle4()
    clock.current_cycle += 1

clock = Clock()

# ++++++++++++++++++++++++++++++++++++++++++++++==

for i in range(10):    
    step_cycle()
    #mir.debug()
    print(scratchpad.registers["a"].output().unsigned)
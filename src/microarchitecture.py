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

serialize("programs/interpreter.mic1", [
    Bit32(0b00010000110000000000000000000000), #0
    Bit32(0b00000000010100000110000000000000), #1
    Bit32(0b10110000000100110000000000011100), #2
    Bit32(0b00100100000101000011001100010011), #3
    Bit32(0b00110100000101000000010000001011), #4
    Bit32(0b00110000000000000000010000001001), #5
    Bit32(0b00010000110000000011000000000000), #6
    Bit32(0b00000000010000000000000000000000), #7
    Bit32(0b11110000000100010000000000000000), #8
    Bit32(0b00010001101000000011000100000000), #9
    Bit32(0b01100000001000000000000000000000), #10
    Bit32(0b00110000000000000000010000001111), #11
    Bit32(0b00000000110000000011000000000000), #12
    Bit32(0b00000000010000000000000000000000), #13
    Bit32(0b11100000000100010001000000000000), #14
    Bit32(0b00010000110000000011000000000000), #15
    Bit32(0b00000000010100010110000100000000), #16
    Bit32(0b10011000000110100000000000000000), #17
    Bit32(0b01100000000100011010000100000000), #18
    Bit32(0b00110100000101000000010000011001), #19
    Bit32(0b00110000000000000000010000010111), #20
    Bit32(0b00110000000000000000000100000000), #21
    Bit32(0b01101000000100000011100000000000), #22
    Bit32(0b01010000000000000000000100010110), #23
    Bit32(0b01100000000000000000000000000000), #24
    Bit32(0b00110000000000000000010000011011), #25
    Bit32(0b01101000000100000011100000000000), #26
    Bit32(0b01101000000100010011100000000000), #27
    Bit32(0b00100100000101000011001100101000), #28
    Bit32(0b00110100000101000000010000100011), #29
    Bit32(0b00110000000000000000010000100001), #30
    Bit32(0b00000000000110100011001000000000), #31
    Bit32(0b01100000110000001010000000000111), #32
    Bit32(0b00000000000110100011001000000000), #33
    Bit32(0b01110001101000001010000100001010), #34
    Bit32(0b00110000000000000000010000100110), #35
    Bit32(0b00000000000110100011001000000000), #36
    Bit32(0b01100000110000001010000000001101), #37
    Bit32(0b00000000000110100011001000000000), #38
    Bit32(0b01100000110000001010000000010000), #39
    Bit32(0b00110100000101000000010000101110), #40
    Bit32(0b00110000000000000000010000101100), #41
    Bit32(0b00110000000000000000000100010110), #42
    Bit32(0b01100000000000000000000000000000), #43
    Bit32(0b01010000000000000000000100000000), #44
    Bit32(0b01101000000100000011100000000000), #45
    Bit32(0b00110100000101000000010000110010), #46
    Bit32(0b00000000000100100010011100000000), #47
    Bit32(0b00010001101000000010000000000000), #48
    Bit32(0b01101000001100000011100000000000), #49
    Bit32(0b00110100000101000000010001000001), #50
    Bit32(0b00110100000101000000010000111011), #51
    Bit32(0b00110000000000000000010000111000), #52
    Bit32(0b00000000110000000001000000000000), #53
    Bit32(0b00000000010100100010011100000000), #54
    Bit32(0b01100000101000000010000000001010), #55
    Bit32(0b00000000110100100010011000000000), #56
    Bit32(0b00000000010000000000000000000000), #57
    Bit32(0b01100000101000000001000000001010), #58
    Bit32(0b00110000000000000000010000111110), #59
    Bit32(0b00000000000100100010011100000000), #60
    Bit32(0b01110001101000000010000100001010), #61
    Bit32(0b00000000110100100010011000000000), #62
    Bit32(0b00000000010000000000000000000000), #63
    Bit32(0b11110000000100010000000000000000), #64
    Bit32(0b00110100000101000000010001001001), #65
    Bit32(0b00110000000000000000010001000110), #66
    Bit32(0b00000000110100100010011000000000), #67
    Bit32(0b00000000010000000000000000000000), #68
    Bit32(0b11110000000100000000000000000000), #69
    Bit32(0b00010000000110100000000100000000), #70
    Bit32(0b00010000000100010000001000000000), #71
    Bit32(0b01110000000100100000101000000000), #72
    Bit32(0b00110000000000000000010001001100), #73
    Bit32(0b00001000000110100011100100000000), #74
    Bit32(0b01100000000100100010101000000000), #75
    Bit32(0b00001000000110100011100100000000), #76
    Bit32(0b00011000000110100000101000000000), #77
    Bit32(0b01100000000110101010011001001011)  #78
])

serialize("programs/program.mic1", [
    assemble_microinstruction(),
    assemble_microinstruction(enc=1, c=9, b=5, a=4),                     # load 1 into "a"
    assemble_microinstruction(cond=3, enc=1, c=9, b=5, a=9, addr=2),     # while(true): "a" += 1
])

serialize("programs/fibonacci.mic1", [
    assemble_microinstruction(),

    assemble_microinstruction(enc=1, c=9, a=5, alu=2),
    assemble_microinstruction(enc=1, c=10, a=5, alu=2),

    assemble_microinstruction(enc=1, c=9, a=10, b=9),
    assemble_microinstruction(enc=1, c=10, a=9, b=10, cond=3, addr=3),
])

cs.load_microprogram(deserialize("programs/fibonacci.mic1"))

step_cycle()  
step_cycle()  
for i in range(10):  
    step_cycle()  
    print(scratchpad.registers["a"].output().unsigned)
    step_cycle()  
    print(scratchpad.registers["b"].output().unsigned)
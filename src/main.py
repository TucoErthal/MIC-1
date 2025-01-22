from nicegui import ui
from components import *

# ================================ DATAPATH ================================

mem = Memory()

scratchpad : RegisterFile = RegisterFile()
latch_A = Latch16()
latch_B = Latch16()
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
sh.input = alu.output                   #ALU TO SHIFTER
scratchpad.input = sh.output            #SHIFTER TO SCRATCHPAD

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
cs.mpc = mpc.output
mir.input = cs.output
ms.input_cond = mir.cond
ms.input_negative_flag = alu.negative_flag
ms.input_zero_flag = alu.zero_flag

# to datapath
scratchpad.addr_A = mir.bus_A
scratchpad.addr_B = mir.bus_B
scratchpad.addr_C = mir.bus_C

amux.select = mir.amux
alu.opcode = mir.alu
sh.opcode = mir.shift

def reset():
    mem.generate_garbage()
    update_memory_table()

    scratchpad.reset()
    update_scratchpad_table()

    clock.current_cycle = 1
    clock.current_subcycle = 1

def update_memory_table():
    memory_table.update_rows(
        [
            {"address": f"0x{(base_address + i):03x}", "value": byte.unsigned} for i, byte in enumerate(mem.bytes)
        ]
    )
def update_scratchpad_table():
        scratchpad_table.update_rows(
            [
                {
                    'register': name,
                    'unsigned_value': register.output.unsigned,
                    'signed_value': register.output.signed
                } for name, register in scratchpad.registers.items()
            ]
        )
def update_mir_table():
        mir_table.update_rows(
            [
                {
                    'name': "amux", 'amux': mir.amux.unsigned,
                    'name': "cond", 'cond': mir.cond.unsigned,
                    'name': "alu", 'alu': mir.alu.unsigned,
                    'name': "shift", 'shift': mir.shift.unsigned,
                    'name': "mbr", 'mbr': mir.mbr.unsigned,
                    'name': "mar", 'mar': mir.mar.unsigned,
                    'name': "rd", 'rd': mir.rd.unsigned,
                    'name': "wr", 'wr': mir.wr.unsigned,
                    'name': "encode_C", 'encode_C': mir.encode_C.unsigned,
                    'name': "bus_C", 'bus_C': mir.bus_C.unsigned,
                    'name': "bus_B", 'bus_B': mir.bus_B.unsigned,
                    'name': "bus_A", 'bus_A': mir.bus_A.unsigned,
                    'name': "addr", 'addr': mir.addr.unsigned
                }
            ]
        )

# ================================ CLOCK ================================

class Clock:
    def __init__(self):
        self.current_cycle = 1
        self.current_subcycle = 1

def subcycle1():
    mir.update()
    update_mir_table()
    ui.notify("subcycle 1")

def subcycle2():
    latch_B.input = scratchpad.output_B
    latch_B.update()    
    ui.notify("subcycle 2")

def subcycle3():
    ui.notify("subcycle 3")

def subcycle4():    
    scratchpad.update()
    update_scratchpad_table()
    """ 
    print("scratchpad.registers[a]", scratchpad.registers["a"])
    print("scratchpad.input", scratchpad.input.unsigned)
    print("sh.output", sh.output.unsigned)
    print("alu.input_A", alu.input_A.unsigned)
    print("alu.input_B", alu.input_B.unsigned)
    print("alu.opcode", alu.opcode.unsigned)
    print("latch_A.output", latch_A.output.unsigned)
    
    print("scratchpad.output_A", scratchpad.output_A.unsigned)
    print("scratchpad.output_B", scratchpad.output_B.unsigned) """

    ui.notify("subcycle 4")
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

# ====================== USER INTERFACE ======================

def throw_error(message: str):
    ui.notify(message, color="red")

with ui.column(align_items="center").classes('w-full'):
    with ui.row():
        ui.label().classes("h-128").bind_text_from(clock, "current_cycle")
        ui.toggle({1: '1', 2: '2', 3: '3', 4: '4'}).bind_value_from(clock, "current_subcycle")

    with ui.button_group():
        with ui.button(icon = "play_arrow", on_click = step_subcycle).classes('bg-grey'):
            ui.tooltip("Step subcycle")

        with ui.button(icon = "skip_next", on_click = step_cycle).classes('bg-grey'):
            ui.tooltip("Step cycle")

        with ui.button(icon = "power_settings_new", on_click = reset).classes('bg-red'):
            ui.tooltip("Reset").classes('bg-red')

with ui.row():
    base_address = 0xf00
    memory_table = ui.table(
        rows = [
            {"address": f"0x{(base_address + i):03x}", "value": byte.unsigned} for i, byte in enumerate(mem.bytes)
        ],
        row_key="address"
    )
        
    """ scratchpad.registers["pc"].output = Bit16(1<<15)
    scratchpad.registers["sp"].output = Bit16((1<<16)-1) """
    scratchpad_table = ui.table(
        columns = [
            {'name': 'register', 'label': 'Register', 'field': 'register', 'align': 'left', 'sortable': False},
            {'name': 'value', 'label': 'Unsigned', 'field': 'unsigned_value', 'align': 'left', 'sortable': False},
            {'name': 'value', 'label': 'Signed', 'field': 'signed_value', 'align': 'left', 'sortable': False},
        ],
        rows = [
            {
                'register': name,
                'unsigned_value': register.output.unsigned,
                'signed_value': register.output.signed
            } for name, register in scratchpad.registers.items()
        ]
    )

    with ui.column():
        mir_table = ui.table(
            title = "MIR",
            column_defaults = {
                'align': 'left',
                'sortable': False
            },
            columns = [
                {'name': 'amux',        'label': 'AMUX',    'field': 'amux'},
                {'name': 'cond',        'label': 'COND',    'field': 'cond'},
                {'name': 'alu',         'label': 'ALU',     'field': 'alu'},
                {'name': 'shift',       'label': 'SHIFT',   'field': 'shift'},
                {'name': 'mbr',         'label': 'MBR',     'field': 'mbr'},
                {'name': 'mar',         'label': 'MAR',     'field': 'mar'},
                {'name': 'rd',          'label': 'RD',      'field': 'rd'},
                {'name': 'wr',          'label': 'WR',      'field': 'wr'},
                {'name': 'encode_C',    'label': 'ENC_C',   'field': 'encode_C'},
                {'name': 'bus_C',       'label': 'C',       'field': 'bus_C'},
                {'name': 'bus_B',       'label': 'B',       'field': 'bus_B'},
                {'name': 'bus_A',       'label': 'A',       'field': 'bus_A'},
                {'name': 'addr',        'label': 'ADDR',    'field': 'addr'}
            ],
            rows = [
                {
                    'name': "amux", 'amux': mir.amux.unsigned,
                    'name': "cond", 'cond': mir.cond.unsigned,
                    'name': "alu", 'alu': mir.alu.unsigned,
                    'name': "shift", 'shift': mir.shift.unsigned,
                    'name': "mbr", 'mbr': mir.mbr.unsigned,
                    'name': "mar", 'mar': mir.mar.unsigned,
                    'name': "rd", 'rd': mir.rd.unsigned,
                    'name': "wr", 'wr': mir.wr.unsigned,
                    'name': "encode_C", 'encode_C': mir.encode_C.unsigned,
                    'name': "bus_C", 'bus_C': mir.bus_C.unsigned,
                    'name': "bus_B", 'bus_B': mir.bus_B.unsigned,
                    'name': "bus_A", 'bus_A': mir.bus_A.unsigned,
                    'name': "addr", 'addr': mir.addr.unsigned
                }
            ]
        )
        ui.button("+20, update", on_click=update_mir_table)
        with ui.column().classes('w-full'):
            def modify_microprogram():
                cs.microprogram = [Bit32(int(microinstruction)) for microinstruction in editor.value]
                print(cs.microprogram)
            editor = ui.codemirror(value = "type here", language="C", theme="basicDark", on_change = modify_microprogram).classes('w-full')
            
ui.run(port=8080)
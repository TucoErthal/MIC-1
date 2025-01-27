from nicegui import ui, events
from microarchitecture import *

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
                    'unsigned_value': register.output().unsigned,
                    'signed_value': register.output().signed
                } for name, register in scratchpad.registers.items()
            ]
        )
def update_mir_table():
        mir_table.update_rows(
            [
                {
                    'name': "amux", 'amux': mir.amux().unsigned,
                    'name': "cond", 'cond': mir.cond().unsigned,
                    'name': "alu", 'alu': mir.alu().unsigned,
                    'name': "shift", 'shift': mir.sh().unsigned,
                    'name': "mbr", 'mbr': mir.mbr().unsigned,
                    'name': "mar", 'mar': mir.mar().unsigned,
                    'name': "rd", 'rd': mir.rd().unsigned,
                    'name': "wr", 'wr': mir.wr().unsigned,
                    'name': "encode_C", 'encode_C': mir.enc().unsigned,
                    'name': "bus_C", 'bus_C': mir.c().unsigned,
                    'name': "bus_B", 'bus_B': mir.b().unsigned,
                    'name': "bus_A", 'bus_A': mir.a().unsigned,
                    'name': "addr", 'addr': mir.addr().unsigned
                }
            ]
        )

# ====================== USER INTERFACE ======================

def step_subcycle():
    match(clock.current_subcycle):
        case 0 | 4:
            subcycle1()
            step_cycle_button.disable()
        case 1:
            subcycle2()
            step_cycle_button.disable()
        case 2:
            subcycle3()
            step_cycle_button.disable()
        case 3:
            subcycle4()
            step_cycle_button.enable()
        case _: pass

def step_cycle():
    _delay = 0.1
    step_subcycle_gui()
    ui.timer(_delay, step_subcycle_gui, once=True)
    ui.timer(2 * _delay, step_subcycle_gui, once=True)
    ui.timer(3 * _delay, step_subcycle_gui, once=True)
    
def step_subcycle_gui():
    step_subcycle()
    update_scratchpad_table()
    update_mir_table()

def step_cycle_gui():
    step_cycle()
    update_memory_table()
    update_scratchpad_table()
    update_mir_table()     

def reset_gui():
    reset()
    step_cycle_button.enable()
    update_memory_table()
    update_scratchpad_table()
    update_mir_table()

with ui.column(align_items="center").classes('w-full'):
    with ui.row():
        with ui.button(color="grey"):                
            ui.label().style('font-weight: 512').bind_text_from(clock, "current_cycle")
            
        ui.toggle({1: '1', 2: '2', 3: '3', 4: '4'}).bind_value_from(clock, "current_subcycle")

        with ui.button_group():
            with ui.button(icon = "play_arrow", on_click = step_subcycle_gui) as step_subcycle_button:
                ui.tooltip("Step subcycle")

            with ui.button(icon = "skip_next", on_click = step_cycle_gui) as step_cycle_button:
                ui.tooltip("Step cycle")

            with ui.button(icon = "power_settings_new", on_click = reset_gui).classes('bg-red'):
                ui.tooltip("Reset").classes('bg-red')

with ui.row():
    base_address = 0xf00
    memory_table = ui.table(
        rows = [
            {"address": f"0x{(base_address + i):03x}", "value": byte.unsigned} for i, byte in enumerate(mem.bytes)
        ],
        row_key="address"
    )
        
    scratchpad_table = ui.table(
        columns = [
            {'name': 'register', 'label': 'Register', 'field': 'register', 'align': 'left', 'sortable': False},
            {'name': 'value', 'label': 'Unsigned', 'field': 'unsigned_value', 'align': 'left', 'sortable': False},
            {'name': 'value', 'label': 'Signed', 'field': 'signed_value', 'align': 'left', 'sortable': False},
        ],
        rows = [
            {
                'register': name,
                'unsigned_value': register.output().unsigned,
                'signed_value': register.output().signed
            } for name, register in scratchpad.registers.items()
        ]
    )

    with ui.column().classes('min-w-[33vw]'):
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
                    'name': "amux", 'amux': mir.amux().unsigned,
                    'name': "cond", 'cond': mir.cond().unsigned,
                    'name': "alu", 'alu': mir.alu().unsigned,
                    'name': "shift", 'shift': mir.sh().unsigned,
                    'name': "mbr", 'mbr': mir.mbr().unsigned,
                    'name': "mar", 'mar': mir.mar().unsigned,
                    'name': "rd", 'rd': mir.rd().unsigned,
                    'name': "wr", 'wr': mir.wr().unsigned,
                    'name': "encode_C", 'encode_C': mir.enc().unsigned,
                    'name': "bus_C", 'bus_C': mir.c().unsigned,
                    'name': "bus_B", 'bus_B': mir.b().unsigned,
                    'name': "bus_A", 'bus_A': mir.a().unsigned,
                    'name': "addr", 'addr': mir.addr().unsigned
                }
            ]
        ).classes('w-full')
        
        microprogram_preview = ui.markdown("")

        def handle_upload(e: events.UploadEventArguments):
            microprogram = deserialize(e.content)
            content = ""
            for microinstruction in microprogram:
                content += f"{microinstruction.unsigned:032b}\n\n"
            microprogram_preview.set_content(content)
            microprogram_preview.update()
            cs.load_microprogram(microprogram)
            reset_gui()

        ui.upload(on_upload=handle_upload).props('accept=.mic1')

    with ui.card().classes('w-[20vw]'):
        ui.image('assets/subcycle0.png').bind_visibility_from(clock, "current_subcycle", value = 0)
        ui.image('assets/subcycle1.png').bind_visibility_from(clock, "current_subcycle", value = 1)
        ui.image('assets/subcycle2.png').bind_visibility_from(clock, "current_subcycle", value = 2)
        ui.image('assets/subcycle3.png').bind_visibility_from(clock, "current_subcycle", value = 3)
        ui.image('assets/subcycle4.png').bind_visibility_from(clock, "current_subcycle", value = 4)


ui.run(port=8080)
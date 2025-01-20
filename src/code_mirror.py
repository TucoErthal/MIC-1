from nicegui import ui

is_simulation_running = False
running_button = ui.icon("stop", size="64px")

def change_text():
    if(is_simulation_running == True):
        set_execution_state(False)
        ui.notify("Program changed. Execution stopped")
    preview.content = editor.value

def set_execution_state(should_run : bool):
    print(f"running = {should_run}")
    global is_simulation_running
    is_simulation_running = should_run
    running_button.name = "play_arrow" if should_run else "stop"

preview = ui.markdown()

editor = ui.codemirror(value = "type here", language="C", theme="basicDark", on_change = change_text).classes('h-32')

ui.button(on_click = lambda: set_execution_state(True), icon = "power_settings_new")

# List of bytes (values)

byte_values = [18, 21, 123, 8, 123, 6, 4, 34, 7, 123, 7, 666, 1]
base_address = 0xf00
rows = [{"address": f"0x{(base_address + i):03x}", "value": byte} for i, byte in enumerate(byte_values)]

# Create a table with the rows
ui.table(rows=rows, row_key="address")

ui.run()
program = open("macroprogram.asm", "r")

for line_zero_indexed, instruction in enumerate(program.readlines()):
    line = line_zero_indexed + 1
    instruction = instruction.strip()  # Remove leading/trailing whitespace

    if instruction.isspace():
        continue

    # Stop processing at "//" for inline comments
    if "//" in instruction:
        instruction = instruction.split("//", 1)[0].strip()

    tokens = instruction.split()
    if not tokens:  # If the line becomes empty after removing comments
        continue

    if len(tokens) == 2:
        print("line", line, "INST(ARG): \t", instruction)

    elif len(tokens) == 1:
        print("line", line, "INST(): \t", instruction)

    else:
        print("line", line, "SYNTAX ERROR")








    
"""
se começa com "//":
    é um comentario
else:
    se tiver um ":":
        é uma flag
    else:
        se tiver mais de uma palavra:
            é uma instrução de 1 operando
        else:
            é uma instrução de 0 operandos

syntax error
"""
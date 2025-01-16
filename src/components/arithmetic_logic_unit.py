class ArithmeticLogicUnit:
    """
    F = 00: R = A + B
    F = 01: R = A & B
    F = 10: R = A
    F = 11: R = INV(A)
    """
    def __init__(self):
        self.opcode = 0b00
        input_A = 0b00000000
        input_B = 0b00000000

    @property
    def result(self):
        match(self.opcode):
            case 0b00: # ADD
                return self.input_A + self.input_B
            
            case 0b00: # AND
                return self.input_A & self.input_B
            
            case 0b00: # PASS
                return self.input_A
            
            case 0b00: # NOT
                return ~ self.input_A
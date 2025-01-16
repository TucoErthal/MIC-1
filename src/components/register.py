from bitstring import BitArray

class Register:
    def __init__(self, width):
        self.input = BitArray(length = width)
        self.output = BitArray(length = width)
        self.write = BitArray(length = 1)

    def update(self): # Acts as clock pin
        if(self.write.uint):
            self.output.overwrite(self.input, 0)



"""
# ================ TESTS ====================
reg1 = Register(width = 8) # cria um registrador de 8 bits
print(reg1.output) # deve printar 0 em binario

reg1.input.overwrite(BitArray(uint = 9, length = 8), 0)
reg1.write.overwrite(BitArray(uint = 1, length = 1), 0) # write
reg1.update()
print(reg1.output) # deve printar 9 em hex

reg1.input.overwrite(BitArray(uint = 4, length = 8), 0)
reg1.write.overwrite(BitArray(uint = 1, length = 1), 0) # write
reg1.update()
print(reg1.output) # deve printar 4 em hex

reg1.input.overwrite(BitArray(uint = 254, length = 8), 0)
reg1.write.overwrite(BitArray(uint = 1, length = 1), 0) #dont write anymore
reg1.update()
print(reg1.output) # deve printar 4 em hex """
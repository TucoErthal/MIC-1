class BitmaskExample:
    def __init__(self):
        self.original_value = 0

    @property
    def bitmask(self):
        return self.original_value & 0b1111

obj = BitmaskExample()
obj.original_value = 0b11111111
print(f"Original Value: {obj.original_value}")
print(f"Bitmask: {obj.bitmask}")

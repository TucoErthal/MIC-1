VERBOSE_DEBUG = True

def bit_slice(value : int, offset : int, width : int,):
    mask = (1 << width) - 1
    return (value >> offset) & mask

def check_range(value : int, width : int):
    if not(0 <= value <= (1 << width) - 1):
        raise ValueError(f"{value} out of range for {width} bits")

def uint_to_int(value: int, bit_count: int) -> int:
    mask = (1 << bit_count) - 1
    value &= mask
    if value & (1 << (bit_count - 1)):
        return value - (1 << bit_count)
    return value

# ============================================================================

class Bit:
    def __init__(self, width: int, value: int):
        check_range(value, width)
        self._width = width
        self._value = value

    @property
    def unsigned(self) -> int:
        return self._value
    
    @property
    def signed(self) -> int:
        return uint_to_int(self._value, self._width)
        
class Bit1(Bit):
    def __init__(self, value: int):
        super().__init__(1, value)
        
class Bit2(Bit):
    def __init__(self, value: int):
        super().__init__(2, value)
        
class Bit4(Bit):
    def __init__(self, value: int):
        super().__init__(4, value)
        
class Bit8(Bit):
    def __init__(self, value: int):
        super().__init__(8, value)
        
class Bit12(Bit):
    def __init__(self, value: int):
        super().__init__(12, value)
        
class Bit16(Bit):
    def __init__(self, value: int):
        super().__init__(16, value)
        
class Bit32(Bit):
    def __init__(self, value: int):
        super().__init__(32, value)
        
# =========== TESTS =================
""" a = Bit32(4294967295)
print(a.unsigned)
print(a.signed)

a = Bit32(2147483648)
print(a.unsigned)
print(a.signed)

a = Bit2(3)
print(a.unsigned)
print(a.signed) """
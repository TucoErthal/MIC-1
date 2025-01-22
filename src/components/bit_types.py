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

class Bit1:
    def __init__(self, value: int):
        check_range(value, 1)
        self._value = value

    @property
    def unsigned(self) -> int:
        return self._value
    
        
class Bit2:
    def __init__(self, value: int):
        check_range(value, 2)
        self._value = value

    @property
    def unsigned(self) -> int:
        return self._value
    
    @property
    def signed(self) -> int:
        return uint_to_int(self._value, 2)
        
class Bit4:
    def __init__(self, value: int):
        check_range(value, 4)
        self._value = value

    @property
    def unsigned(self) -> int:
        return self._value
    
    @property
    def signed(self) -> int:
        return uint_to_int(self._value, 4)
        
class Bit8:
    def __init__(self, value: int):
        check_range(value, 8)
        self._value = value

    @property
    def unsigned(self) -> int:
        return self._value
    
    @property
    def signed(self) -> int:
        return uint_to_int(self._value, 8)
        
class Bit12:
    def __init__(self, value: int):
        check_range(value, 12)
        self._value = value

    @property
    def unsigned(self) -> int:
        return self._value
    
    @property
    def signed(self) -> int:
        return uint_to_int(self._value, 12)
        
class Bit16:
    def __init__(self, value: int):
        check_range(value, 16)
        self._value = value

    @property
    def unsigned(self) -> int:
        return self._value
    
    @property
    def signed(self) -> int:
        return uint_to_int(self._value, 16)
        
class Bit32:
    def __init__(self, value: int):
        check_range(value, 32)
        self._value = value

    @property
    def unsigned(self) -> int:
        return self._value
    
    @property
    def signed(self) -> int:
        return uint_to_int(self._value, 32)
        
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
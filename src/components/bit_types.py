def bit_slice(value : int, offset : int, width : int,):
    mask = (1 << width) - 1
    return (value >> offset) & mask

class UInt1:
    def __init__(self, value: int, override : bool = False):
        if(0 <= value <= 1):
            self.value = value
        elif(override == False):
            raise ValueError("assigned value out of range for UInt1")
    
    def set(self, value : int):
        if(0 <= value <= 1):
            self.value = value
        else:
            raise ValueError("assigned value out of range for UInt1")
    
        
class UInt2:
    def __init__(self, value: int, override : bool = False):
        if(0 <= value <= (1 << 2) - 1):
            self.value = value
        elif(override == False):
            raise ValueError(f"{value} out of range for UInt2")

    def set(self, value : int):
        if(0 <= value <= (1 << 2) - 1):
            self.value = value
        else:
            raise ValueError(f"{value} out of range for UInt2")
        
class UInt4:
    def __init__(self, value: int, override : bool = False):
        if(0 <= value <= (1 << 4) - 1):
            self.value = value
        elif(override == False):
            raise ValueError(f"{value} out of range for UInt4")

    def set(self, value : int):
        if(0 <= value <= (1 << 4) - 1):
            self.value = value
        else:
            raise ValueError(f"{value} out of range for UInt4")
        
class UInt8:
    def __init__(self, value: int, override : bool = False):
        if(0 <= value <= (1 << 8) - 1):
            self.value = value
        elif(override == False):
            raise ValueError(f"{value} out of range for UInt8")

    def set(self, value : int):
        if(0 <= value <= (1 << 8) - 1):
            self.value = value
        else:
            raise ValueError(f"{value} out of range for UInt8")
        
class UInt12:
    def __init__(self, value: int, override : bool = False):
        if(0 <= value <= (1 << 12) - 1):
            self.value = value
        elif(override == False):
            raise ValueError(f"{value} out of range for UInt12")

    def set(self, value : int):
        if(0 <= value <= (1 << 12) - 1):
            self.value = value
        else:
            raise ValueError(f"{value} out of range for UInt12")
        
class UInt16:
    def __init__(self, value: int, override : bool = False):
        if(0 <= value <= (1 << 16) - 1):
            self.value = value
        elif(override == False):
            raise ValueError(f"{value} out of range for UInt16")

    def set(self, value : int):
        if(0 <= value <= (1 << 16) - 1):
            self.value = value
        else:
            raise ValueError(f"{value} out of range for UInt16")
        
class UInt32:
    def __init__(self, value: int, override : bool = False):
        if(0 <= value <= (1 << 32) - 1):
            self.value = value
        elif(override == False):
            raise ValueError(f"{value} out of range for UInt32")

    def set(self, value : int):
        if(0 <= value <= (1 << 32) - 1):
            self.value = value
        else:
            raise ValueError(f"{value} out of range for UInt32")
        
# ================= INT ================

class Int12:
    def __init__(self, value: int, override : bool = False):
        if(-(1 << 11) <= value <= (1 << 11) - 1):
            self.value = value
        elif(override == False):
            raise ValueError(f"{value} out of range for Int12")

    def set(self, value : int):
        if(-(1 << 11) <= value <= (1 << 11) - 1):
            self.value = value
        else:
            raise ValueError(f"{value} out of range for Int12")

class Int16:
    def __init__(self, value: int, override : bool = False):
        if(-(1 << 15) <= value <= (1 << 15) - 1):
            self.value = value
        elif(override == False):
            raise ValueError(f"{value} out of range for Int16")

    def set(self, value : int):
        if(-(1 << 15) <= value <= (1 << 15) - 1):
            self.value = value
        else:
            raise ValueError(f"{value} out of range for Int16")
        
class Int32:
    def __init__(self, value: int, override : bool = False):
        if(-(1 << 31) <= value <= (1 << 31) - 1):
            self.value = value
        elif(override == False):
            raise ValueError(f"{value} out of range for Int32")

    def set(self, value : int):
        if(-(1 << 31) <= value <= (1 << 31) - 1):
            self.value = value
        else:
            raise ValueError(f"{value} out of range for Int32")
        
""" # =========== TESTS =================
a = UInt8(10)
b = a
a.set(255)
print(b.value) """
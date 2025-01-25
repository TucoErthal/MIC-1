from .bit_types import *

class ControlStore:
    def __init__(self):
        self._microprogram : list[Bit32] = []

    def load_microprogram(self, microprogram : list[Bit32]):
        self._microprogram = microprogram

    def input(self) -> Bit8:
        raise ConnectionError("Input unconnected")

    def output(self) -> Bit32:
        _input = self.input()
        _output = self._microprogram[_input.unsigned]
        if VERBOSE_DEBUG: print(f"\tcs({_input.unsigned}) = {_output.unsigned:08x}\t@ {self}")
        return _output
    
def test():
    print("TEST 2: control_store")
    cs = ControlStore()
    cs.load_microprogram([Bit32(0xfeedbeef)])
    cs.input = lambda: Bit8(0)
    cs.output()


    """     microinstruction(),                                                             # 0: mar:=pc; rd;                                         Busca
            microinstruction(),                                                             # 1: pc:=pc + 1; rd;                                      Busca
            microinstruction(),                                                             # 2: ir:=mbr; if n then goto 28;                          Busca/Identifica
            microinstruction(),                                                             # 3: tir:=lshift(ir + ir); if n then goto 19;             Identifica
            microinstruction(),                                                             # 4: tir:=lshift(tir); if n then goto 11;                 Identifica
            microinstruction(),                                                             # 5: alu:=tir; if n then goto 9;                          Identifica
            # ================================ 0000 = LODD ================================
            microinstruction(),                                                             # 6: mar:=ir; rd;                                         Executa 
            microinstruction(),                                                             # 7: rd;                                                  Executa
            microinstruction(),                                                             # 8: ac:=mbr; goto 0;                                     Executa
            # ================================ 0001 = STOD ================================
            microinstruction(),                                                             # 9: mar:=ir; mbr:=ac; wr;                                
            microinstruction(),                                                             # 10: wr; goto 0;                                         Executa
            microinstruction(),                                                             # 11: alu:=tir; if n then goto 15;                        Identifica
            # ================================ 0010 = ADDD ================================
            microinstruction(),                                                             # 12: mar:=ir; rd;                                        
            microinstruction(),                                                             # 13: rd;                                                 Executa
            microinstruction(),                                                             # 14: ac:=mbr + ac; goto 0;                               Executa
            # ================================ 0011 = SUBD ================================
            microinstruction(),                                                             # 15: mar:=ir; rd;                                        
            microinstruction(),                                                             # 16: ac:=ac + 1; rd;                                     Executa
            microinstruction(),                                                             # 17: a:=inv(mbr);                                        Executa
            microinstruction(),                                                             # 18: ac:=ac + a; goto 0;                                 Executa
            microinstruction(),                                                             # 19: tir:=lshift(tir); if n then goto 25;                Identifica
            microinstruction(),                                                             # 20: alu:=tir; if n then goto 23;
            # ================================ 0100 = JPOS ================================
            microinstruction(),                                                             # 21: alu:=ac; if n then goto 0;                          
            microinstruction(),                                                             # 22: pc:=band(ir,amask); goto 0;
            # ================================ 0101 = JZER ================================
            microinstruction(),                                                             # 23: alu:=ac; if z then goto 22;                         
            microinstruction(),                                                             # 24: goto 0;
            microinstruction(),                                                             # 25: alu:=tir; if n then goto 27;
            # ================================ 0110 = JUMP ================================
            microinstruction(),                                                             # 26: pc:=band(ir,amask); goto 0;                         
            # ================================ 0111 = LOCO ================================
            microinstruction(),                                                             # 27: ac:=band(ir,amask); goto 0;                         
            microinstruction(),                                                             # 28: tir:=lshift(ir + ir); if n then goto 40;
            microinstruction(),                                                             # 29: tir:=lshift(tir); if n then goto 35;
            microinstruction(),                                                             # 30: alu:=tir; if n then goto 33;
            # ================================ 1000 = LODL ================================
            microinstruction(),                                                             # 31: a:=ir + sp;                                         
            microinstruction(),                                                             # 32: mar:=a; rd; goto 7;                                       
            # ================================ 1001 = STOL ================================
            microinstruction(),                                                             # 33: a:=ir + sp;  
            microinstruction(),                                                             # 34: mar:=a; mbr:=ac; wr; goto 10;
            microinstruction(),                                                             # 35: alu:=tir; if n then goto 38;
            # ================================ 1010 = ADDL ================================
            microinstruction(),                                                             # 36: a:=ir + sp;                                         
            microinstruction(),                                                             # 37: mar:=a; rd; goto 13;
            # ================================ 1011 = SUBL ================================
            microinstruction(),                                                             # 38: a:=ir + sp;                                         
            microinstruction(),                                                             # 39: mar:=a; rd; goto 16 ;
            microinstruction(),                                                             # 40: tir:=lshift(tir); if n then goto 46;
            microinstruction(),                                                             # 41: alu:=tir; if n then goto 44;
            # ================================ 1100 = JNEG ================================
            microinstruction(),                                                             # 42: alu:=ac; if n then goto 22;                         
            microinstruction(),                                                             # 43: goto 0;
            # ================================ 1101 = JNZE ================================
            microinstruction(),                                                             # 44: alu:=ac; if z then goto 0;                          
            microinstruction(),                                                             # 45: pc:=band(ir,amask); goto 0;
            microinstruction(),                                                             # 46: tir:=lshift(tir); if n then goto 50;
            # ================================ 1110 = CALL ================================
            microinstruction(),                                                             # 47: sp:=sp + (-1);                                      
            microinstruction(),                                                             # 48: mar:=sp; mbr:=pc; wr;
            microinstruction(),                                                             # 49: pc:=band(ir,amask); wr; goto 0;
            microinstruction(),                                                             # 50: tir:=lshift(tir); if n then goto 65;
            microinstruction(),                                                             # 51: tir:=lshift(tir); if n then goto 59;
            microinstruction(),                                                             # 52: alu:=tir; if n then goto 56;
            # ================================ 1111 0000 = PSHI ================================
            microinstruction(),                                                             # 53: mar:=ac; rd;                                        
            microinstruction(),                                                             # 54: sp:=sp + (-1); rd;
            microinstruction(),                                                             # 55: mar:=sp; wr; goto 10;
            # ================================ 1111 0010 = POPI ================================
            microinstruction(),                                                             # 56: mar:=sp; sp:=sp + 1; rd;                            
            microinstruction(),                                                             # 57: rd;
            microinstruction(),                                                             # 58: mar:=ac; wr; goto 10;
            microinstruction(),                                                             # 59: alu:=tir; if n then goto 62;
            # ================================ 1111 0100 = PUSH ================================
            microinstruction(),                                                             # 60: sp:=sp + (-1);                                      
            microinstruction(),                                                             # 61: mar:=sp; mbr:=ac; wr; goto 10;
            # ================================ 1111 0110 = POP ================================
            microinstruction(),                                                             # 62: mar:=sp; sp:=sp + 1; rd;                            
            microinstruction(),                                                             # 63: rd;
            microinstruction(),                                                             # 64: ac:=mbr; goto 0;
            microinstruction(),                                                             # 65: tir:=lshift(tir); if n then goto 73;
            microinstruction(),                                                             # 66: alu:=tir; if n then goto 70;
            # ================================ 1111 1000 = RETN ================================
            microinstruction(),                                                             # 67: mar:=sp; sp:=sp + 1; rd;                            
            microinstruction(),                                                             # 68: rd;
            microinstruction(),                                                             # 69: pc:=mbr; goto 0;
            # ================================ 1111 1010 = SWAP ================================
            microinstruction(),                                                             # 70: a:=ac;                                              
            microinstruction(),                                                             # 71: ac:=sp;
            microinstruction(),                                                             # 72: sp:=a; goto 0;
            microinstruction(),                                                             # 73: alu:=tir; if n then goto 76;
            # ================================ 1111 1100 = INSP ================================
            microinstruction(),                                                             # 74: a:=band(ir,smask);                                  
            microinstruction(),                                                             # 75: sp:=sp + a; goto 0;
            # ================================ 1111 1110 = DESP ================================
            microinstruction(),                                                             # 76: a:=band(ir, smask);                                 
            microinstruction(),                                                             # 77: a:=inv(a);
            microinstruction(),                                                             # 78: a:=a + 1; goto 75; """
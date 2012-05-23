reg = {"pc":0, "acc":0}

def parse_reg(reg):
        return reg.split("h")[0]

mem = []
stack = []

def i_acall(addr):
        stack.push(reg["pc"])
        reg["pc"] = addr
        
def i_add(arg):
        reg["acc"] += arg

def i_addc(arg):
        #TODO

def i_ajmp(addr):
        reg["pc"] = addr
        
def i_anl(arg0, arg1):
        reg[arg0] &= arg1
       
def i_cjne(op0, op1, reladdr):
        if op0[0] == '@':
                op0 = mem[reg[op0[1:]]]
        elif op0[0] == 'r':
                op0 = mem[reg[op0]]
        elif op0 == 'a':
                op0 =  reg['a']

        if op1[0] == '#':
                op1 = int(op1[1:])
        else:
                op1 = mem[int(op1)]
                
        if op0 != op1:
               reg['pc'] += reladdr 
        
def i_clr(register):
        if register[0] == "a":
                reg["a"] = 0
        elif register[0] == "c":
                reg["c"] = 0
        else:
                addr = int(parse_reg(register), 16)
                addr_byte = (0x20 + addr) / 8
                bit_offset = addr % 8
                mem[addr_byte] &= (0xff - (1 << (bit_offset)))
                
def i_cpl(register):
        if register[0] == "a":
                reg["a"] = 0xff - reg["a"]
        elif register[0] == "c":
                reg["c"] = 0xff - reg["c"]
        else:
                addr = int(parse_reg(register), 16)
                addr_byte = (0x20 + addr) / 8
                bit_offset = addr % 8
                if(mem[addr_byte] & (0xff - (1 << (bit_offset)))):
                        mem[addr_byte] -= 1 << (bit_offset)
                else:
                        mem[addr_byte] += 1 << (bit_offset)

def i_da(reg):
        if()

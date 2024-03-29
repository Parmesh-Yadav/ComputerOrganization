import sys


def convert_bs(v, i):
    # v is the value to be converted from integer to binary string
    # i is the number of bits - 8 or 16

    b = str(bin(v))
    b = b[2:]
    
    if len(b) != i:
        b = "0" * (i - len(b)) + b
    

    return b

def convert_int(v):
     # v is the value to be converted from binary string to integer
     b = int(v, 2)
     
     return b



op_commands = {
    "00000"  : "add",  #add
    "00001"  : "sub",  #subtract
    "00010" : "movi",  #move immediate
    "00011" : "movr",  #move register
    "00100"   : "ld",  #load
    "00101"   : "st",  #store
    "00110"  : "mul",  #multiply
    "00111"  : "div",  #division
    "01000"   : "rs",  #right shift
    "01001"   : "ls",  #left shift
    "01010"  : "xor",  #bitwise exclusive OR
    "01011"   : "or",  #bitwise OR
    "01100"  : "and",  #bitwise AND  
    "01101"  : "not",  #bitwise NOT
    "01110"  : "cmp",  #compare
    "01111"  : "jmp",  #jump (unconditional)
    "10000"  : "jlt",  #jump (if less than)
    "10001"  : "jgt",  #jump (if greater to)
    "10010"   : "je",  #jump (if equal to)
    "10011"  : "hlt"   #halt
}

registers = {
    "000" : 0, 
    "001" : 0,
    "010" : 0,
    "011" : 0,
    "100" : 0,
    "101" : 0,
    "110" : 0,
    "111" : [0,0,0,0]
}

variables = {}

isFlagChange = False

pc = 0


def set_flag_v(final_value):
    
    global isFlagChange

    if final_value > 255:
        registers["111"][0] = 1
        isFlagChange = True
        

def set_flag_l(r1_v,r2_v):

    global isFlagChange

    if(r1_v < r2_v):
        registers["111"][1] = 1
        isFlagChange = True
        return True
        
        
def set_flag_g(r1_v,r2_v):
    global isFlagChange

    if(r1_v > r2_v):
        registers["111"][2] = 1
        isFlagChange = True
        return True
        
        
def set_flag_e(r1_v,r2_v):
    
    global isFlagChange

    if(r1_v == r2_v):
        registers["111"][3] = 1
        isFlagChange = True
        return True
    
    

def add(line):

    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:]

    registers[r1] = registers[r2] + registers[r3]
    set_flag_v(registers[r1])
    
def sub(line):
    
    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:]

    registers[r1] = registers[r2] - registers[r3]
    set_flag_v(registers[r1])
    
def movi(line):
    
    r1 = line[5:8]
    v = line[8:]
    
    registers[r1] = convert_int(v)
    
def movr(line):
    
    r1 = line[10:13]
    r2 = line[13:]

    if r2 == "111":
        a = "0" * 8
        for x in registers["111"]:
            a += str(x)
        
        registers[r1] = int(a)
    else:
        registers[r1] = registers[r2]
    
def load(line):

    r1 = line[5:8]
    mem_add = line[8:]

    if mem_add not in variables.keys():
        variables[mem_add] = 0
    
    
    registers[r1] = variables[mem_add]

    return None

def store(line):
    r1 = line[5:8]
    mem_add = line[8:]

    variables[mem_add] = registers[r1]

    return None


def multiply(line):

    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:]

    registers[r1] = registers[r2] * registers[r3]
    
    set_flag_v(registers[r1])


def divide(line):
    quotient = 0 #stores the quotient
    remainder = 0 #stores the remainder

    r2 = line[10:13] #first register in input
    r3 = line[13:] #second register in input

    remainder = registers[r2] // registers[r3] #floor division

    quotient = registers[r2] % registers[r3] #storing the remainder

    registers["000"] = quotient # R0 = quotient
    registers["001"] = remainder # R1 = remainder


def jump_less(line):
    global pc
    
    if registers["111"][1] == "1":
        #we need to update the program counter
        pc += convert_int(line[8:]) #integer value of line[8:]

    

def jump_greater(line):
    global pc

    if registers["111"][2] == "1":

        pc+=convert_int(line[8:]) #integer value of the line[8:]
    

def jump_equal(line):
    global pc

    if registers["111"][3] == "1":
        pc+=convert_int(line[8:])



def rs(line):
    
    r1 = line[5:8]
    v = line[8:]
    
    registers[r1] = registers[r1] >> v

def ls(line):
    
    r1 = line[5:8]
    v = line[8:]
    
    registers[r1] = registers[r1] << v




def xor(line):

    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:]

    registers[r1] = registers[r2] ^ registers[r3]

def Or(line):

    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:]

    registers[r1] = registers[r2] | registers[r3]

def And(line):

    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:]

    registers[r1] = registers[r2] & registers[r3]

def Not(line):
    
    r1 = line[10:13]
    r2 = line[13:]
    
    registers[r1] = not registers[r2]

def cmp(line):
    
    r1 = line[10:13]
    r2 = line[13:]
    
    # registers[r1] == registers[r2]
    if(set_flag_l(registers[r1],registers[r2])):
        None
    elif(set_flag_g(registers[r1],registers[r2])):
        None
    elif(set_flag_e(registers[r1],registers[r2])):
        None       
    
    

def jump(line):
    global pc
    
    #we need to update the program counter
    pc += convert_int(line[8:]) #integer value of line[8:]

def decode_command(line,pc):

    halted = False
    PC = pc

    opcode = line[0:5]

    if op_commands[opcode] == "add":
        add(line)
    
    elif op_commands[opcode] == "sub":
        sub(line)
        
    elif op_commands[opcode] == "movi":
        movi(line)

    elif op_commands[opcode] == "movr":
        movr(line)
    
    elif op_commands[opcode] == "rs":
        rs(line)
    
    elif op_commands[opcode] == "ls":
        ls(line)
        
    elif op_commands[opcode] == "xor":
        xor(line)
        
    elif op_commands[opcode] == "or":
        Or(line)

    elif op_commands[opcode] == "and":
        And(line)

    elif op_commands[opcode] == "ld":
        load(line)

    elif op_commands[opcode] == "st":
        store(line)
    
    elif op_commands[opcode] == "mul":
        multiply(line)

    elif op_commands[opcode] == "div":
        divide(line)

    elif op_commands[opcode] == "not":
        Not(line)
    
    elif op_commands[opcode] == "cmp":
        cmp(line)

    elif op_commands[opcode] == "jmp":
        jump(line)

    elif op_commands[opcode] == "jlt":
        jump_less(line)
    
    elif op_commands[opcode] == "jgt":
        jump_greater(line)
    
    elif op_commands[opcode] == "je":
        jump_equal(line)


    elif op_commands[opcode] == "hlt":
        halted = True
        #function not needed

    global isFlagChange

    if isFlagChange == False:
        registers["111"] = [0,0,0,0]
    else:
        isFlagChange = False

    if PC == pc:
        PC += 1
    return halted, PC

    
    

def print_registers():

    #lst = registers.values()

    for x in registers:
        if x != "111":
           # print(registers[x])
            print(convert_bs(registers[x],16),end = " ")

    

        
def print_flag_register():
    flag = "0"*12
    for i in registers["111"]:
        flag = flag + str(i)
    print(flag)
    


def memory_dump(input_list):
   
   count = 0

   for line in input_list:
       print(line)
       count+=1

   for var in variables:
        print(convert_bs(variables[var], 16) )
        count+=1
    
   while count <= 255:
        print("0" * 16)
        count+=1
   
   return None


def main():
    
    complete_input = sys.stdin.read()
    input_list = complete_input.split('\n')

    # input_list = []
    # while(True):
    #     x = input()

    #     if(x ==  "hlt"):
    #         break
        
    #     input_list.append(x)
    
    halted = False

    global pc

    # for line in input_list:
    while not halted:
        # if not halted:
        line = input_list[pc]
        

        halted,updated_pc = decode_command(line,pc)
        

        print(convert_bs(pc,8), end = " ")
        print_registers()
        print_flag_register()
        
        pc = updated_pc

    memory_dump(input_list)





if __name__ == '__main__':
    main() 
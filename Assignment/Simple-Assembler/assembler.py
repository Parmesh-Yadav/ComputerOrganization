import sys



op_commands = {
    "add"  : "00000",  #add
    "sub"  : "00001",  #subtract
    "movi" : "00010",  #move immediate
    "movr" : "00011",  #move register
    "ld"   : "00100",  #load
    "st"   : "00100",  #store
    "mul"  : "00110",  #multiply
    "div"  : "00111",  #division
    "rs"   : "01000",  #right shift
    "ls"   : "01001",  #left shift
    "xor"  : "01010",  #bitwise exclusive OR
    "or"   : "01011",  #bitwise AND
    "not"  : "01101",  #bitwise NOT
    "cmp"  : "01110",  #compare
    "jmp"  : "01111",  #jump (unconditional)
    "jlt"  : "10000",  #jump (if less than)
    "jgt"  : "10001",  #jump (if greater to)
    "je"   : "10010",  #jump (if equal to)
    "hlt"  : "10011"   #halt
}

registers = {
    "R0":  "000",
    "R1" : "001",
    "R2" : "010",
    "R3":  "011",
    "R4" : "100",
    "R5" : "101",
    "R6" : "110"
}

def main():
    get_input()
    

if __name__ == '__main__':
    main()




def get_input():
    
    complete_input = sys.stdin.read()
    
    input_list = complete_input.split('/n')
    
    output_s = ""
    
    
    for line in input_list:
        inp = line.split(' ')
        #inst means instruction that the user gave

        if(inp[0] == "add"):
            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]
            output_s = output_s + add(r1,r2,r3)
            output_s = output_s + "/n"

        elif(inp[0] == "sub"):
            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]
            output_s = output_s + sub(r1,r2,r3)
            output_s = output_s + "/n"


        elif(inp[0] == "mov"):
            if(inp[2][0] == "$"):
                r1 = inp[1]
                imm = int(inp[2][1:]) # casting the value into an integer

                output_s = output_s + move_immediate(r1, imm)
                output_s = output_s + "/n"

            else:
                r1 = inp[1]
                r2 = inp[2]
                output_s = output_s + move_register(r1,r2)
                output_s = output_s + "/n"


        
        elif(inp[0] == ""):
            None


        elif(inp[0] == ""):
            None


        elif(inp[0] == "div"):
            r3 = inp[1]
            r4 = inp[2]
            output_s = output_s + divide(r3, r4)
            output_s = output_s + "/n"



        elif(inp[0] == "ls"):
            r1 = inp[1]
            v = inp[2]
            v = int(v[1:])
            output_s = output_s + leftshift(r1, v)
            output_s = output_s + "/n"



        elif(inp[0] == "rs"):
            r1 = inp[1]
            v = inp[2]
            v = int(v[1:])
            output_s = output_s + rightshift(r1, v)
            output_s = output_s + "/n"



        elif(inp[0] == ""):
            None


        elif(inp[0] == ""):
            None


        elif(inp[0] == ""):
            None


        elif(inp[0] == ""):
            None


        elif(inp[0] == ""):
            None


        elif(inp[0] == ""):
            None


        elif(inp[0] == ""):
            None
        
        

#MARK: add function

def add(r1,r2,r3):
    # r1 = r2 + r3
    # opcode(5) + unused(2) + r1(3) + r2(3) + r3(3)

    opcode = "00001"
    unused = "00"

    a = registers[r1] #first register opcode
    b = registers[r2] #second register opcode
    c = registers[r3] #third register opcode
    
    machine_code = opcode + unused + a + b + c
    
    return machine_code




#MARK: subtract function

def sub(r1,r2,r3):
    # r1 = r2 - r3
    # opcode(5) + unused(2) + r1(3) + r2(3) + r3(3)
    opcode = op_commands["sub"]
    unused = "00"

    a = registers[r1] #first register opcode
    b = registers[r2] #second register opcode
    c = registers[r3] #third register opcode

    machine_code = opcode + unused + a + b + c
    return machine_code




#MARK: move immediate

def move_immediate(r1, imm):

    # move the value imm into the register r1
    # opcode(5) + reg1(3) + immediate_value(8)

    opcode = op_commands["movi"]
    
    a = registers[r1] #register opcode
    b = str(bin(imm))
    b = b[2:]
    if(len(b) != 8):
        b = 0*(8-len(b)) + b

    machine_code = opcode + a + b

    return machine_code




#MARK: move register

def move_register(r1, r2):

    # performs r1 = r2
    # opcode(5) + unused(5) + r1(3) + r2(3)

    opcode = op_commands["movr"]
    unused = "00000"
    a = registers[r1]
    b = registers[r2]

    machine_code = opcode + unused + a + b

    return machine_code






#MARK: division fucntion

def divide(r3,r4):
    # opcode(5) + unused(5) + r3(3) + r4(3)

    opcode = op_commands['div']
    unused = "0"*5

    a = registers[r3] #first register opcode
    b = registers[r4] #second register opcode
    
    machine_code = opcode + unused + a + b
    
    return machine_code


#MARK: leftshift fucntion

def leftshift(r1,v):
    # opcode(5) + r1(3) + value(8)

    opcode = op_commands['ls']
    
    a = registers[r1] #first register opcode
    b = str(bin(v))
    b = b[2:]
    if len(b) != 8:
        b = "0"*(8-len(b)) + b
    
    machine_code = opcode + a + b
    
    return machine_code


#MARK: rightshift fucntion

def rightshift(r1,v):
    # opcode(5) + r1(3) + value(8)

    opcode = op_commands['rs']
    
    a = registers[r1] #first register opcode
    b = str(bin(v))
    if len(b) != 8:
        b = "0"*(8-len(b)) + b
    
    machine_code = opcode + a + b
    
    return machine_code
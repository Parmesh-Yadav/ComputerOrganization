import sys

def count_var(input_list):
    count = 0
    for i in input_list:

        line = i.split(' ')

        if(line[0] == 'var'):
            count += 1

    return count
            
    

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
    "R6" : "110",
    "FLAGS": "111"
}

variables = {}
labels = {}

def get_labels(input_list):
    
    line_no = 0
    for line in input_list:

        inp = line.split(' ')

        if(len(inp[0])!=0 and inp[0][-1] == ':'):
            line_no_b = str(bin(line_no))
            line_no_b = line_no_b[2:]

            if len(line_no_b) != 8:
                line_no_b = "0"*(8-len(line_no_b)) + line_no_b

            label = inp[0]
            label = label[:-1]

            labels[label] = line_no_b

        line_no += 1




def get_input():
    
    complete_input = sys.stdin.read()
    
    input_list = complete_input.split('\n')
    
    output_s = ""
    
    var_count = count_var(input_list)
    var_index = len(input_list) - var_count    

    line_no = 0

    get_labels(input_list)
    
    for line in input_list:
        
        inp = line.split(' ')
        
        if(len(inp[0])!=0 and inp[0][-1] == ':'):
            inp.remove(inp[0])

        if(inp[0] == "add"):
            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]
            output_s = output_s + add(r1,r2,r3)
            output_s = output_s + "\n"

        elif(inp[0] == "sub"):
            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]
            output_s = output_s + sub(r1,r2,r3)
            output_s = output_s + "\n"


        elif(inp[0] == "mov"):

            if(inp[2][0] == "$"):
                imm = int(inp[2][1:]) # casting the value into an integer
                r1 = inp[1]
                output_s = output_s + move_immediate(r1, imm)
                output_s = output_s + "\n"

            else:
                r1 = inp[1]
                r2 = inp[2]
                output_s = output_s + move_register(r1,r2)
                output_s = output_s + "\n"



        elif(inp[0] == "ld"):
            
            r1 = inp[1]
            var = inp[2]
            bvar = str(bin(var_index))
            bvar = bvar[2:]
            

            if(len(bvar) != 8):
                bvar = ("0" * (8-len(bvar)) ) + bvar

            variables[var] = bvar
            var_index += 1

            output_s = output_s + load(r1,bvar)
            output_s = output_s + "\n"


        elif (inp[0] == "st"):
            r1 = inp[1]
            var = inp[2]
            bvar = str(bin(var_index))
            bvar = bvar[2:]

            if(len(bvar) != 8):
                bvar = ("0" * (8-len(bvar)) ) + bvar

            variables[var] = bvar
            var_index += 1

            output_s = output_s + store(r1,var)
            output_s = output_s + "\n"



        elif(inp[0] == "mul"):
            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]
            output_s = output_s + mul(r1,r2,r3)
            output_s = output_s + "\n"


        elif(inp[0] == "div"):
            r3 = inp[1]
            r4 = inp[2]
            output_s = output_s + divide(r3, r4)
            output_s = output_s + "\n"



        elif(inp[0] == "ls"):
            r1 = inp[1]
            v = int(inp[2][1:])
            
            output_s = output_s + leftshift(r1,v)
            output_s = output_s + "\n"
            



        elif(inp[0] == "rs"):
            r1 = inp[1]
            v = int(inp[2][1:])
            
            output_s = output_s + rightshift(r1,v)
            output_s = output_s + "\n"
           

        elif(inp[0] == "xor"):
            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]
            output_s = output_s + xor(r1,r2,r3)
            output_s = output_s + "\n"


        elif(inp[0] == "or"):
            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]
            output_s = output_s + Or(r1,r2,r3)
            output_s = output_s + "\n"


        elif(inp[0] == "and"):
            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]
            output_s = output_s + And(r1,r2,r3)
            output_s = output_s + "\n"

        elif(inp[0] == "not"):
            r1 = inp[1]
            r2 = inp[2]
            output_s = output_s + inverse(r1,r2,r3)
            output_s = output_s + "\n"


        elif(inp[0] == "cmp"):
            r1 = inp[1]
            r2 = inp[2]
            output_s = output_s + compare(r1,r2)
            output_s = output_s + "\n"




        elif(inp[0] == "jmp"):
            mem_add = inp[1]
            output_s = output_s + jump(mem_add)
            output_s = output_s + "\n"


        elif(inp[0] == "jlt"):
            mem_add = inp[1]
            output_s = output_s + jump_less(mem_add)
            output_s = output_s + "\n"
        

        elif(inp[0] == "jgt"):
            mem_add = inp[1]
            output_s = output_s + jump_greater(mem_add)
            output_s = output_s + "\n"

        
        elif(inp[0] == "je"):
            mem_add = inp[1]
            output_s = output_s + jump_equal(mem_add)
            output_s = output_s + "\n"
        

        elif(inp[0] == "hlt"):
            output_s = output_s + hlt()
            output_s = output_s + "\n"
        
        if(inp[0] != "var"):
            line_no += 1

    print(output_s)

        

#MARK: add function

def add(r1,r2,r3):
    # r1 = r2 + r3
    # opcode(5) + unused(2) + r1(3) + r2(3) + r3(3)

    opcode = op_commands["add"]
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
        b = ("0" * (8-len(b)) ) + b

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







#MARK: load function

def load(r1, bvar):
    # opcode(5) + reg(3) + memory_address(8)
    
    opcode = op_commands['ld']
    a = registers[r1]
    v = bvar
    
    machine_code = opcode + a + v
    
    return machine_code





#MARK: store function


def store(r1, var):
    # opcode(5) + reg(3) + memory_address(8)
    
    opcode = op_commands['st']
    a = registers[r1]
    v = variables[var]
    
    machine_code = opcode + a + v
    
    return machine_code







#MARK: multiplication fucntion

def mul(r1,r2,r3):
    # r1 = r2 * r3
    # opcode(5) + unused(2) + r1(3) + r2(3) + r3(3)

    opcode = op_commands['mul']
    unused = "00"

    a = registers[r1] #first register opcode
    b = registers[r2] #second register opcode
    c = registers[r3] #third register opcode
    
    machine_code = opcode + unused + a + b + c
    
    return machine_code








#MARK: division fucntion

def divide(r3,r4):
    # opcode(5) + unused(5) + r3(3) + r4(3)

    opcode =  op_commands['div']
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








#MARK: exclusive or function

def xor(r1,r2,r3):
    # r1 = r2 xor r3
    # opcode(5) + unused(2) + r1(3) + r2(3) + r3(3)

    opcode = op_commands['xor']
    unused = "00"

    a = registers[r1] #first register opcode
    b = registers[r2] #second register opcode
    c = registers[r3] #third register opcode
    
    machine_code = opcode + unused + a + b + c
    
    return machine_code






#MARK: or function

def Or(r1,r2,r3):
    # r1 = r2 | r3
    # opcode(5) + unused(2) + r1(3) + r2(3) + r3(3)

    opcode = op_commands['or']
    unused = "00"

    a = registers[r1] #first register opcode
    b = registers[r2] #second register opcode
    c = registers[r3] #third register opcode
    
    machine_code = opcode + unused + a + b + c
    
    return machine_code






#MARK: and function

def And(r1,r2,r3):
    # r1 = r2 & r3
    # opcode(5) + unused(2) + r1(3) + r2(3) + r3(3)

    opcode = op_commands['and']
    unused = "00"

    a = registers[r1] #first register opcode
    b = registers[r2] #second register opcode
    c = registers[r3] #third register opcode
    
    machine_code = opcode + unused + a + b + c
    
    return machine_code






#MARK: inverse function -- bitwise not

def inverse(r1,r2):
    #opcode(5) + unused(5) + r1(3) + r2(3)
    opcode = op_commands["not"]

    unused = "0" * 5
    r1 = registers[r1]
    r2 = registers[r2]

    machine_code = opcode + unused + r1 + r2

    return machine_code







#MARK: compare function

def compare(r1,r2):

    #opcode(5) + unused(5) + r1(3) + r2(3)

    opcode = op_commands["cmp"] 
    unused = "0" * 5
    r1 = registers[r1]
    r2 = registers[r2]

    machine_code = opcode + unused + r1 + r2

    return machine_code




#MAR: Jump unconditional 

def jump(mem_add):
    #opcode(5) + unused(3) + address(8)
    
    opcode = op_commands["jmp"]
    unused = "0" * 3
    address = labels[mem_add]
    
    machine_code = opcode + unused + address

    return machine_code
    



#MARK: jump if less than
def jump_less(mem_add):
    #opcode(5) + unused(3) + address(8)
    
    opcode = op_commands["jlt"]
    unused = "0" * 3
    address = labels[mem_add]
    
    machine_code = opcode + unused + address

    return machine_code



#MARK: Jump if greater than

def jump_greater(mem_add):
    #opcode(5) + unused(3) + address(8)
    
    opcode = op_commands["jgt"]
    unused = "0" * 3
    address = labels[mem_add]
    
    machine_code = opcode + unused + address

    return machine_code

#MARK: Jump if equal

def jump_equal(mem_add):
    #opcode(5) + unused(3) + address(8)
    
    opcode = op_commands["je"]
    unused = "0" * 3
    address = labels[mem_add]
    
    machine_code = opcode + unused + address

    return machine_code



#MARK: halt function

def hlt():
    #stops machine from executing
    # opcode(5) + unused(11)

    opcode = op_commands['hlt']
    unused = "0"*11

    machine_code = opcode + unused

    return machine_code



def main():
    get_input()
    

if __name__ == '__main__':
    main()
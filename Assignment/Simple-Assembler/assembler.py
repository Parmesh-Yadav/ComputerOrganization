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
    "st"   : "00101",  #store
    "mul"  : "00110",  #multiply
    "div"  : "00111",  #division
    "rs"   : "01000",  #right shift
    "ls"   : "01001",  #left shift
    "xor"  : "01010",  #bitwise exclusive OR
    "or"   : "01011",  #bitwise OR
    "and"  : "01100",  #bitwise AND  
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

        if(inp[0] != "var"):
            line_no += 1




def get_variables(input_list):
    for line in input_list:
        inp = line.split(' ')

        if inp[0] == 'var' and len(inp) !=1 :
            
            variables[inp[1]] = 0
    


def check_halt_as_last(input_list, var_count):
   
    last_line = input_list[-1].split(' ')

    if(last_line[0] == "hlt" or len(last_line) == 0): 
        return False

    elif(len(last_line[0]) !=0 and last_line[0][-1] == ':'):
        if(last_line[1] == "hlt"):
            return False

    print('hlt not being used as the last instruction at line ', (len(input_list) - var_count - 1))
    return True



def count_halt(input_list, var_count):
    count = 0

    for line in input_list:
        inp = line.split(' ')
        if inp[0] == 'hlt':
            count += 1

        elif(len(inp[0]) !=0 and inp[0][-1] == ':'):
            if(len(inp) !=1 and inp[1] == "hlt"):
                count+=1

    if count == 1:
        return False
    print('There are ' + str(count) + ' Halt instructions' + ' at line ' + str(len(input_list) - var_count - 1))
    return True



def var_beg(input_list):
    var_occ = -1
    instr_occ = 0
    line_no = 0
    for line in input_list:
        inp = line.split(' ')
        if inp[0] == 'var':
            var_occ = line_no
            break
        line_no += 1
    
    line_no = 0
    for line in input_list:
        inp = line.split(' ')

        if(inp[0] != 'var'):
            instr_occ = line_no
            break

        line_no += 1

    if(var_occ < instr_occ):
        return False

    print("Invalid variable declaration at line ", line_no)

    return True      


def check_label(input_list):

    line_no = 0

    for line in input_list:
        inp = line.split(' ')

        if(inp[0] in ["jmp", "jgt", "jlt", "je"]):
            if inp[1] not in labels.keys():
                print("invalid label use at line ", line_no)
                return True
        line_no+=1
                

    return False





def get_input():
    
    complete_input = sys.stdin.read()
    
    input_list = complete_input.split('\n')

    
    # input_list = []
    # while(True):
    #     x = input()

    #     if(x ==  "hlt"):
    #         break
        
    #     input_list.append(x)

    
    output_s = ""

    error = False

    get_labels(input_list)
    get_variables(input_list)

    var_count = count_var(input_list)

    error = count_halt(input_list, var_count) or check_halt_as_last(input_list, var_count) or var_beg(input_list) or check_label(input_list)
    
    var_index = len(input_list) - var_count 

    line_no = 0

    



    if error == True:
        return None


    for line in input_list:
        
        inp = line.split(' ')
        

        if(len(inp[0])!=0 and inp[0][-1] == ':'):
            inp.remove(inp[0])

        if inp[0] not in op_commands.keys():
            if inp[0] not in ['var', 'mov']:
                print("Invalid command ", " at line " , line_no)
                break

        if(inp[0] == "add"):

            if len(inp) != 4:
                print("invalid instruction type for type A", " at line " , line_no)
                break

            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]

            if r1 not in registers.keys() or r2 not in registers.keys() or r3 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS' or r2 == 'FLAGS' or r3 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            output_s = output_s + add(r1,r2,r3)
            output_s = output_s + "\n"

        elif(inp[0] == "sub"):
            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]

            if len(inp) != 4:
                print("invalid instruction type for type A", " at line " , line_no)
                break

            if r1 not in registers.keys() or r2 not in registers.keys() or r3 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS' or r2 == 'FLAGS' or r3 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            
            output_s = output_s + sub(r1,r2,r3)
            output_s = output_s + "\n"


        elif(inp[0] == "mov"):


            if(inp[2][0] == "$"):


                if len(inp) != 3:
                    print("invalid instruction type for type B", " at line " , line_no)
                    break


                imm = int(inp[2][1:]) # casting the value into an integer
                r1 = inp[1]

            
                if r1 not in registers.keys():
                    print("Invalid register use", " at line " , line_no)
                    break
                
                if r1 == 'FLAGS':
                    print('Illegal use of FLAGS register', " at line " , line_no)
                    break
                
                if imm>255 or imm<0:
                    print("Illegal Immediate value", " at line " , line_no)
                    break
                
                output_s = output_s + move_immediate(r1, imm)
                output_s = output_s + "\n"

            else:

                if len(inp) != 3:
                    print("invalid instruction type for type C", " at line " , line_no)
                    break

                r1 = inp[1]
                r2 = inp[2]


                if r1 not in registers.keys() or r2 not in registers.keys():
                    print("Invalid register use", " at line " , line_no)
                    break
                
                if r1 == 'FLAGS':
                    print('Illegal use of FLAGS register', " at line " , line_no)
                    break
                
                output_s = output_s + move_register(r1,r2)
                output_s = output_s + "\n"



        elif(inp[0] == "ld"):

            if len(inp) != 3:
                    print("invalid instruction type for type D", " at line " , line_no)
                    break

            
            r1 = inp[1]
            var = inp[2]

            if r1 not in registers.keys() :
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break

            if var in labels.keys():
                print("label being used as variable", " at line " , line_no)
                break
            
            bvar = str(bin(var_index))
            bvar = bvar[2:]
            

            if(len(bvar) != 8):
                bvar = ("0" * (8-len(bvar)) ) + bvar

            if var not in variables.keys():
                print("variable not declared", " at line " , line_no)
                break


            variables[var] = bvar
            var_index += 1

            output_s = output_s + load(r1,bvar)
            output_s = output_s + "\n"


        elif (inp[0] == "st"):
            
            if len(inp) != 3:
                    print("invalid instruction type for type D", " at line " , line_no)
                    break

            r1 = inp[1]
            var = inp[2]
            
            if r1 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            if r1 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break

            if var in labels.keys():
                print("label being used as variable", " at line " , line_no)
                break

            bvar = str(bin(var_index))
            bvar = bvar[2:]

            # print(var_index, var_count, len(input_list))

            if(len(bvar) != 8):
                bvar = ("0" * (8-len(bvar)) ) + bvar


            if var not in variables.keys():
                print("variable not declared", " at line " , line_no)
                break


            variables[var] = bvar
            var_index += 1

            output_s = output_s + store(r1,var)
            output_s = output_s + "\n"



        elif(inp[0] == "mul"):

            if len(inp) != 4:
                    print("invalid instruction type for type A", " at line " , line_no)
                    break

            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]


            if r1 not in registers.keys() or r2 not in registers.keys() or r3 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS' or r2 == 'FLAGS' or r3 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            output_s = output_s + mul(r1,r2,r3)
            output_s = output_s + "\n"


        elif(inp[0] == "div"):
            
            if len(inp) != 3:
                    print("invalid instruction type for type C", " at line " , line_no)
                    break


            r3 = inp[1]
            r4 = inp[2]

            if r4 not in registers.keys() or r3 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break
            
            if r3 == 'FLAGS' or r4 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            output_s = output_s + divide(r3, r4)
            output_s = output_s + "\n"



        elif(inp[0] == "ls"):

            if len(inp) != 3:
                    print("invalid instruction type for type B", " at line " , line_no)
                    break

            r1 = inp[1]
            v = int(inp[2][1:])

            if r1 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            if v>255 or v<0:
                    print("Illegal Immediate value", " at line " , line_no)
                    break
            
            output_s = output_s + leftshift(r1,v)
            output_s = output_s + "\n"
            



        elif(inp[0] == "rs"):

            if len(inp) != 3:
                    print("invalid instruction type for type B", " at line " , line_no)
                    break

            r1 = inp[1]
            v = int(inp[2][1:])

            if r1 not in registers.keys() :
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            if v>255 or v<0:
                    print("Illegal Immediate value", " at line " , line_no)
                    break
            
            output_s = output_s + rightshift(r1,v)
            output_s = output_s + "\n"
           

        elif(inp[0] == "xor"):

            if len(inp) != 4:
                    print("invalid instruction type for type A", " at line " , line_no)
                    break


            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]

            if r1 not in registers.keys() or r2 not in registers.keys() or r3 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS' or r2 == 'FLAGS' or r3 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            output_s = output_s + xor(r1,r2,r3)
            output_s = output_s + "\n"


        elif(inp[0] == "or"):
            
            if len(inp) != 4:
                    print("invalid instruction type for type A", " at line " , line_no)
                    break


            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]

            if r1 not in registers.keys() or r2 not in registers.keys() or r3 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS' or r2 == 'FLAGS' or r3 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            output_s = output_s + Or(r1,r2,r3)
            output_s = output_s + "\n"


        elif(inp[0] == "and"):

            if len(inp) != 4:
                    print("invalid instruction type for type A", " at line " , line_no)
                    break


            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]

            if r1 not in registers.keys() or r2 not in registers.keys() or r3 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS' or r2 == 'FLAGS' or r3 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            output_s = output_s + And(r1,r2,r3)
            output_s = output_s + "\n"

        elif(inp[0] == "not"):

            if len(inp) != 3:
                    print("invalid instruction type for type C", " at line " , line_no)
                    break

            r1 = inp[1]
            r2 = inp[2]

            if r1 not in registers.keys() or r2 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS' or r2 == 'FLAGS':
                print('Illegal use of FLAGS register', " at line " , line_no)
                break
            
            output_s = output_s + inverse(r1,r2)
            output_s = output_s + "\n"


        elif(inp[0] == "cmp"):

            if len(inp) != 3:
                    print("invalid instruction type for type C", " at line " , line_no)
                    break

            r1 = inp[1]
            r2 = inp[2]

            if r1 not in registers.keys() or r2 not in registers.keys():
                print("Invalid register use", " at line " , line_no)
                break
            
            if r1 == 'FLAGS' or r2 == 'FLAGS':
                print("Illegal use of FLAGS register at line " , line_no)
                break
            
            output_s = output_s + compare(r1,r2)
            output_s = output_s + "\n"




        elif(inp[0] == "jmp"):

            if len(inp) != 2:
                    print("invalid instruction type for type E at line " , line_no)
                    break

            mem_add = inp[1]

            if mem_add in variables.keys():
                print("variable being used as label at line " , line_no)

            output_s = output_s + jump(mem_add)
            output_s = output_s + "\n"


        elif(inp[0] == "jlt"):
            
            if len(inp) != 2:
                    print("invalid instruction type for type E at line " , line_no)
                    break

            mem_add = inp[1]

            if mem_add in variables.keys():
                print("variable being used as label at line " , line_no)

            output_s = output_s + jump_less(mem_add)
            output_s = output_s + "\n"
        

        elif(inp[0] == "jgt"):

            if len(inp) != 2:
                    print("invalid instruction type for type E at line " , line_no)
                    break


            mem_add = inp[1]

            if mem_add in variables.keys():
                print("variable being used as label at line " , line_no)
           
            output_s = output_s + jump_greater(mem_add)
            output_s = output_s + "\n"

        
        elif(inp[0] == "je"):

            if len(inp) != 2:
                    print("invalid instruction type for type E at line " , line_no)
                    break

            mem_add = inp[1]
            
            if mem_add in variables.keys():
                print("variable being used as label at line " , line_no)

            output_s = output_s + jump_equal(mem_add)
            output_s = output_s + "\n"
        

        elif(inp[0] == "hlt"):

            if len(inp) != 1:
                    print("invalid instruction type for type F at line " , line_no)
                    break

            output_s = output_s + hlt()
            output_s = output_s + "\n"

        elif(len(inp) == 0):
            None    
        
        if(inp[0] != "var"):
            line_no += 1
        


    else:
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
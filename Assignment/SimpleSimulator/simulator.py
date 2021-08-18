def convert_bs(v, i):
    # v is the value to be converted from integer to binary string
    # i is the number of bits - 8 or 16.

    b = str(bin(v))
    b = b[2:]
    if len(b) != i:
        b = "0"*(i-len(b)) + b

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
    "111" : "0000" 
}

def add(line):

    r1 = line[7:10]
    r2 = line[10:13]
    r3 = line[13:]

    registers[r1] = registers[r2] + registers[r3]



def decode_command(line):

    opcode = line[0:6]

    if op_commands[opcode] == "add":
        add(line)

    

def print_registers():

    lst = registers.values()

    for x in lst:
        print(convert_bs(x,16))


def main():
    
    complete_input = sys.stdin.read()
    input_list = complete_input.split('\n')

    pc = 0

    for line in input_list:
        
        decode_command(line)
        
        print(convert_bs(pc,8), end = " ")
        
        print_registers()





if __name__ == '__main__':
    main() 
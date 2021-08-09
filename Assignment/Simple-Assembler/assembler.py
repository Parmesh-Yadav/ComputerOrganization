import sys



global op_commands = {
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

global registers = {
    "R0":  "000"
    "R1" : "001"
    "R2" : "010"
    "R3":  "011"
    "R4" : "100"
    "R5" : "101"
    "R6" : "110"
}

def main():
    print(op_commands["add"])
    

if __name__ == '__main__':
    main()




def get_input():
    
    complete_input = sys.stdin.read()
    
    for line in complete_input:
        inst = line.split()
        #inst means instruction that the user gave

        if(inp[0] == "add"):
            r1 = inp[1]
            r2 = inp[2]
            r3 = inp[3]
            add(r0,r1,r2)

        elif(inp[0] == "sub"):
            


        elif(inp[0] == ""):

        
        
        elif(inp[0] == ""):
        

        
        elif(inp[0] == ""):



        elif(inp[0] == ""):



        elif(inp[0] == ""):



        elif(inp[0] == ""):



        elif(inp[0] == ""):



        elif(inp[0] == ""):



        elif(inp[0] == ""):



        elif(inp[0] == ""):



        elif(inp[0] == ""):



        elif(inp[0] == ""):



        elif(inp[0] == ""):



        elif(inp[0] == ""):

        


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
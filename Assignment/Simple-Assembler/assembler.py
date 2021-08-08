





"""
key-value of the opcommands dictionary 
    "add"  : 00000, #add
    "sub"  : 00001, #subtract
    "movi" : 00010, #move immediate
    "movr" : 00011, #move register
    "ld"   : 00100, #load
    "st"   : 00100, #store
    "mul"  : 00110, #multiply
    "div"  : 00111, #divide
    "rs"   : 01000, #right shift
    "ls"   : 01001, #left shift
    "xor"  : 01010, #bitwise exclusive OR
    "or"   : 01011, #bitwise OR
    "and"  : 01100, #bitwise AND
    "not"  : 01101, #bitwise not
    "cmp"  : 01110, #compare
    "jmp"  : 01111, #jump (uncoditional)
    "jlt"  : 10000, #jump (if less than)
    "jgt"  : 10001, #jump (if greater than)
    "je"   : 10010, #jump (if equal to)
    "hlt"  : 10011  #halt

"""
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

def main():
    print(op_commands["add"])
    

if __name__ == '__main__':
    main()
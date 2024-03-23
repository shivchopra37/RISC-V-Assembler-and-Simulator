import sys
final = []
# OPCODES
R_type = {'add': '0110011', 'sub': '0110011', 'sll': '0110011','slt': '0110011', 'sltu': '0110011', 'xor': '0110011','srl': '0110011', 'or': '0110011', 'and': '0110011'}
I_type = {'lw': '0000011', 'addi': '0010011', 'sltiu': '0010011','jalr': '1100111'}
S_type = {'sw': '0100011'}
B_type = {'beq': '1100011','bne': '1100011', 'blt': '1100011', 'bge': '1100011','bltu': '1100011', 'bgeu': '1100011'}
U_type = {'lui': '0110111','auipc': '0010111'}
J_type = {'jal': '1101111'}

# Function-3
R_type_func3 = {'add': '000', 'sub': '000', 'sll': '001','slt': '010', 'sltu': '011', 'xor': '100','srl': '101', 'or': '110', 'and': '111'}
I_type_func3 = {'lw': '010', 'addi': '000', 'sltiu': '011','jalr': '000'}
S_type_func3 = {'sw': '010'}
B_type_func3 = {'beq': '000','bne': '001', 'blt': '100', 'bge': '101','bltu': '110', 'bgeu': '111'}

# Converting decimal to binary
def twos_complement(num):
    return bin(2**12 + num)[2:].zfill(12)
    

def twos_complement_bits(num,bits):
    return bin(num & (2**bits - 1))[2:].zfill(bits)

reg_dict = {
    "zero": "00000", "ra": "00001", "sp": "00010", "gp": "00011", "tp": "00100",
    "t0": "00101", "t1": "00110", "t2": "00111", "s0": "01000", "fp": "01000",
    "s1": "01001", "a0": "01010", "a1": "01011", "a2": "01100", "a3": "01101",
    "a4": "01110", "a5": "01111", "a6": "10000", "a7": "10001", "s2": "10010",
    "s3": "10011", "s4": "10100", "s5": "10101", "s6": "10110", "s7": "10111",
    "s8": "11000", "s9": "11001", "s10": "11010", "s11": "11011", "t3": "11100",
    "t4": "11101", "t5": "11110", "t6": "11111"
}

funct7 = {
    "add":   "0000000", "sub":   "0100000", "sll":   "0000000",
    "slt":   "0000000", "sltu":  "0000000", "xor":   "0000000",
    "srl":   "0000000", "or":    "0000000", "and":   "0000000"
}

def error_R_type(instruction,count):
    if len(instruction)!=4:
        final.append("Error: "+(instruction[0])+" instruction must have 3 parameters, line = "+str(count))
        return 0
    elif instruction[1] not in reg_dict or instruction[2] not in reg_dict or instruction[3] not in reg_dict:
        final.append("Error: No such registers is available, line = "+str(count))
        return 0
    else:
        return 1
    
    
def error_I_type(instruction,count):
    imm_val=instruction[3]
    check = 1
    # print(imm_val)
    if imm_val!="":
        for elt in imm_val:
            if (elt not in '-1234567890'):
                check=0
                break
    else:
        check = 1
    if len(instruction)!=4:
        final.append("Error: "+(instruction[0])+" instruction must have 3 parameters, line = "+str(count))
        return 0
    elif instruction[0] not in I_type:
        final.append("Error : No such instruction in line : "+str(count))
        return 0
    elif instruction[1] not in reg_dict or instruction[2] not in reg_dict:
        final.append("Error: No such registers is available, line = "+str(count))
        return 0
    elif check==0:
        final.append("Error: "+instruction[3]+" is not an immediate value, line = "+str(count))
        return 0 
    elif int(imm_val)<-4096 or int(imm_val)>4095:
        final.append("Error: Immediate values is out of range (12 bits), line = "+str(count))
        return 0
    else:
        return 1
def error_I_type_lw(instruction,count):
    if len(instruction) != 4:
        final.append("Error: " + instruction[0] + " instruction must have 3 parameters, line = " + str(count))
        return False
    elif instruction[0] not in I_type:
        final.append("Error : No such instruction in line : " + str(count))
        return False
    elif instruction[1] not in reg_dict or instruction[3] not in reg_dict:
        final.append("Error: No such registers is available, line = " + str(count))
        return False
    elif not instruction[2].isdigit():
        final.append("Error: " + instruction[3] + " is not an immediate value, line = " + str(count))
        return False
    elif not -2048 <= int(instruction[3]) <= 2047:
        final.append("Error: Immediate value is out of range (-2048 to 2047), line = " + str(count))
        return False
    else:
        return True
def error_S_type(instruction,count):
    imm_val=instruction[2]
    check = 1
    # print(imm_val)
    if imm_val!="":
        for elt in imm_val:
            if elt not in '-1234567890':
                check=0
                break
    else:
        check = 1
    if len(instruction)!=4:
        final.append("Error: "+(instruction[0])+" instruction must have 3 parameters, line = "+str(count))
        return 0
    elif instruction[1] not in reg_dict or instruction[3] not in reg_dict:
        final.append("Error: No such registers is available, line = "+str(count))
        return 0
    elif check==0:
        final.append("Error: "+instruction[2]+" is not an immediate value, line = "+str(count))
        return 0 
    elif int(imm_val)<-4096 or int(imm_val)>4095:
        final.append("Error: Immediate values is out of range (12 bits), line = "+str(count))
        return 0
    else:
        return 1
def error_B_type(instruction,count):
    imm_val=instruction[3]
    check = 1
    if ":" not in instruction[0]:
        if imm_val!="":
            for elt in imm_val:
                if elt not in '-1234567890':
                    check=0
                    break
                else:
                    check = 1
    
    if len(instruction)!=4:
        final.append("Error: "+(instruction[0])+" instruction must have 3 parameters, line = "+str(count))
        return 0
    elif instruction[1] not in reg_dict or instruction[2] not in reg_dict:
        final.append("Error: No such registers is available, line = "+str(count))
        return 0
    elif check==0:
        final.append("Error: "+instruction[3]+" is not an immediate value, line = "+str(count))
        return 0
    elif int(imm_val)<-4096 or int(imm_val)>4095:
        final.append("Error: Immediate values is out of range (12 bits), line = "+str(count))
        return 0
    else:
        return 1
def error_U_type(instruction,count):
    imm_val=instruction[2]
    check = 1
    # print(imm_val)
    if imm_val!="":
        for elt in imm_val:
            if elt not in '-1234567890':
                check=0
                break
    else:
        check = 1
    if len(instruction)!=3:
        final.append("Error: "+(instruction[0])+" instruction must have 2 parameters, line = "+str(count))
        return 0
    elif instruction[0] not in U_type:
        final.append("Error : No such instruction in line : "+str(count))
        return 0
    elif instruction[1] not in reg_dict:
        final.append("Error: No such register is available, line = "+str(count))
        return 0
    elif not -1048576 <= int(instruction[2]) <= 1048575:
        final.append("Error: Immediate value is out of range (-1048576 to 1048575), line = " + str(count))
        return False
    elif check==0:
        final.append("Error: "+instruction[2]+" is not an immediate value, line = "+str(count))
        return 0
    else:
        return True 
def error_J_type(instruction,count):
    imm_val=instruction[2]
    check = 1
    # print(imm_val)
    if imm_val!="":
        for elt in imm_val:
            if elt not in '-1234567890':
                check=0
                break
    else:
        check = 1
    if len(instruction)!=3:
        final.append("Error: "+(instruction[0])+" instruction must have 2 parameters, line = "+str(count))
        return 0
    elif instruction[0] not in J_type:
        final.append("Error : No such instruction in line : "+str(count))
        return 0
    elif instruction[1] not in reg_dict:
        final.append("Error: No such register is available, line = "+str(count))
        return 0
    elif check==0:
        final.append("Error: "+instruction[2]+" is not an immediate value, line = "+str(count))
        return 0 
    elif int(imm_val)<-1048576 or int(imm_val)>1048575:
        final.append("Error: Immediate values is out of range (20 bits), line = "+str(count))
        return 0
    else:
        return 1
line = 0
def instruction_to_machine_code(instruction, count):
    opcode = ""
    func3 = ""
    func7 = ""
    rd = ""
    rs1 = ""
    rs2 = ""
    imm = ""
    
    if ":" in instruction[0]:
        instruction.pop(0)
        
    if instruction[0] in R_type:
        error_R_type(instruction,count)
        opcode = R_type[instruction[0]]
        func3 = R_type_func3[instruction[0]]
        func7 = funct7[instruction[0]]
        rd = reg_dict[instruction[1]]
        rs1 = reg_dict[instruction[2]]
        rs2 = reg_dict[instruction[3]]

        final.append(f"{func7}{rs2}{rs1}{func3}{rd}{opcode}")
        return 
    
    elif instruction[0] in I_type:
        
        if instruction[0] == "lw":
            bracket_handle(instruction)
            error_I_type_lw(instruction,count)
            opcode = I_type[instruction[0]]
            func3 = I_type_func3[instruction[0]]
            rd = reg_dict[instruction[1]]
            rs1 = reg_dict[instruction[3]]
            imm = instruction[2]
            
            final.append(f"{twos_complement(imm)}{rs1}{func3}{rd}{opcode}")
            return f"{twos_complement(imm)}{rs1}{func3}{rd}{opcode}"
        else:
            error_I_type(instruction,count)
            opcode = I_type[instruction[0]]
            func3 = I_type_func3[instruction[0]]
            rd = reg_dict[instruction[1]]
            rs1 = reg_dict[instruction[2]]
            instruction[3] = int(instruction[3])
            imm = instruction[3]
            
            final.append(f"{twos_complement(imm)}{rs1}{func3}{rd}{opcode}")
            return f"{twos_complement(imm)}{rs1}{func3}{rd}{opcode}"
    
    elif instruction[0] in S_type:
        bracket_handle(instruction)
        error_S_type(instruction,count)
        x = twos_complement(instruction[2])
        x = str(x)
        opcode = S_type[instruction[0]]
        func3 = S_type_func3[instruction[0]]
        rs2 = reg_dict[instruction[1]]
        rs1 = reg_dict[instruction[3]]
        
        final.append(f"{x[0:7]}{rs2}{rs1}{func3}{x[7:12]}{opcode}")
        return f"{x[0:7]}{rs2}{rs1}{func3}{x[7:12]}{opcode}"
    
    elif instruction[0] in B_type:
        if instruction[3] not in labels:
            error_B_type(instruction,count)
            opcode = B_type[instruction[0]]
            func3 = B_type_func3[instruction[0]]
            rs2 = reg_dict[instruction[2]]
            rs1 = reg_dict[instruction[1]]
            
            instruction[3] = int(instruction[3])
            x = twos_complement(instruction[3])
            x = str(x)
            
            final.append(f"{x[0]}{x[1:7]}{rs2}{rs1}{func3}{x[8:]}{x[1]}{opcode}")
            return f"{x[0]}{x[1:7]}{rs2}{rs1}{func3}{x[8:]}{x[1]}{opcode}"
        else:
            error_B_type(instruction,count)
            opcode = B_type[instruction[0]]
            func3 = B_type_func3[instruction[0]]
            rs2 = reg_dict[instruction[2]]
            rs1 = reg_dict[instruction[1]]
            x = twos_complement((count - labels[instruction[3]])*4)
            x = str(x)
            final.append(f"{x[0]}{x[1:7]}{rs2}{rs1}{func3}{x[7:11]}{x[1]}{opcode}")
            return f"{x[0]}{x[1:7]}{rs2}{rs1}{func3}{x[7:11]}{x[1]}{opcode}"
    
    
    elif instruction[0] in U_type:
        error_U_type(instruction,count)
        opcode = U_type[instruction[0]]
        register = reg_dict[instruction[1]]
        instruction[2] = int(instruction[2])
        x = twos_complement_bits(instruction[2],32)
        final.append(f"{x[:20]}{register}{opcode}")
        return f"{x[:20]}{register}{opcode}"
    elif instruction[0] in J_type:
        error_J_type(instruction,count)
        opcode = J_type[instruction[0]]
        register = reg_dict[instruction[1]]
        instruction[2] = int(instruction[2])
        x = twos_complement_bits(instruction[2],21)
        x = str(x)
        x1 = x[0]
        x2 = x[10:20]
        x3 = x[9]
        x4 = x[1:9]
        final.append(f"{x1}{x2}{x3}{x4}{register}{opcode}")
        return f"{x1}{x2}{x3}{x4}{register}{opcode}"
    else:
        final.append("Error : No Such instruction found in line : "+str(count))
    
        

# Example usage:
instructions = []
def bracket_handle(instruction):
    lst2 = instruction[2].split("(")
    lst3 = lst2[1].split(")")
    lst3.pop()
    lst2.pop()
    instruction.pop()
    instruction.extend(lst2)
    instruction.extend(lst3)
    instruction[2] = int(instruction[2])
#File Handling 
count = 0
with open("input.txt", "r") as file:
    # Read each line in the file
    for line in file:
        instructions.append(line)
        count+=1
labels={}
variables={}
lines=1
for i in instructions:
    if len(i.split())==0:
        continue
    if ":" in i.split()[0]:
        if (i.split()[0][:-1] in R_type.keys()) or (i.split()[0][:-1] in I_type.keys()) or (i.split()[0][:-1] in S_type.keys()) or (i.split()[0][:-1] in B_type.keys()) or (i.split()[0][:-1] in U_type.keys()) or (i.split()[0][:-1] in J_type.keys()):
            print("Instruction cannot be used as Label")
            sys.exit()
        labels[i.split()[0][:-1]]=lines
        lines+=1

line_Number = 0
for instruction in instructions:
    line_Number+=1
    instruction_parts = [part for part in instruction.strip().split(" ")]
    if len(instruction_parts) == 2:
        lst1 = instruction_parts[1].split(",")
        instruction_parts.pop()
        for i in lst1:
            instruction_parts.append(i)
    else:
        lst1 = instruction_parts[2].split(",")
        instruction_parts.pop()
        for i in lst1:
            instruction_parts.append(i)
    machine_code = instruction_to_machine_code(instruction_parts, line_Number)
counts = 0
with open("output.txt","w") as o:
    for i in final:
        counts+=1
        if counts!=count:
            o.write(i)
            o.write("\n")
        else:
            o.write(i)
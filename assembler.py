import sys
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
    return bin(num & (2**12 - 1))[2:].zfill(12)
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
        opcode = R_type[instruction[0]]
        func3 = R_type_func3[instruction[0]]
        func7 = funct7[instruction[0]]
        rd = reg_dict[instruction[1]]
        rs1 = reg_dict[instruction[2]]
        rs2 = reg_dict[instruction[3]]
        return f"{func7}{rs2}{rs1}{func3}{rd}{opcode}"

    elif instruction[0] in I_type:

        if instruction[0] == "lw":
            bracket_handle(instruction)
            opcode = I_type[instruction[0]]
            func3 = I_type_func3[instruction[0]]
            rd = reg_dict[instruction[1]]
            rs1 = reg_dict[instruction[3]]
            imm = instruction[2]
            return f"{twos_complement(imm)}{rs1}{func3}{rd}{opcode}"
        else:
            opcode = I_type[instruction[0]]
            func3 = I_type_func3[instruction[0]]
            rd = reg_dict[instruction[1]]
            rs1 = reg_dict[instruction[2]]
            instruction[3] = int(instruction[3])
            imm = instruction[3]
            return f"{twos_complement(imm)}{rs1}{func3}{rd}{opcode}"
    elif instruction[0] in S_type:
        bracket_handle(instruction)
        x = twos_complement(instruction[2])
        x = str(x)
        opcode = S_type[instruction[0]]
        func3 = S_type_func3[instruction[0]]
        rs2 = reg_dict[instruction[1]]
        rs1 = reg_dict[instruction[3]]
        return f"{x[0:7]}{rs2}{rs1}{func3}{x[7:12]}{opcode}"
    
    elif instruction[0] in B_type:
        opcode = B_type[instruction[0]]
        func3 = B_type_func3[instruction[0]]
        print(instruction[0])
        print(func3)
        rs2 = reg_dict[instruction[2]]
        rs1 = reg_dict[instruction[1]]
        if instruction[3] not in labels:
            instruction[3] = int(instruction[3])
            x = twos_complement(instruction[3])
            x = str(x)
            
            return f"{x[0]}{x[1:7]}{rs2}{rs1}{func3}{x[8:]}{x[1]}{opcode}"
        else:
            x = twos_complement((count - labels[instruction[3]])*4)
            x = str(x)
            
            return f"{x[0]}{x[1:7]}{rs2}{rs1}{func3}{x[8:]}{x[1]}{opcode}"
    
    
    elif instruction[0] in U_type:
        opcode = U_type[instruction[0]]
        register = reg_dict[instruction[1]]
        instruction[2] = int(instruction[2])
        x = twos_complement_bits(instruction[2],32)
        return f"{x[:20]}{register}{opcode}"

    elif instruction[0] in J_type:
            opcode = J_type[instruction[0]]
            register = reg_dict[instruction[1]]
            instruction[2] = int(instruction[2])
            x = twos_complement_bits(instruction[2],21)
            x = str(x)
            x1 = x[0]
            x2 = x[10:20]
            x3 = x[9]
            x4 = x[1:9]
            return f"{x1}{x2}{x3}{x4}{register}{opcode}"
        
        
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


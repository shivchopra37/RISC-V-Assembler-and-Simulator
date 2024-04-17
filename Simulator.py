#code for R-type instruction
def execute_r_type_instruction(instruction, rd, rs1, rs2, registers):
    if instruction == "ADD":
        registers[rd] = registers[rs1] + registers[rs2]
    elif instruction == "SUB":
        registers[rd] = registers[rs1] - registers[rs2]
    elif instruction == "SLT":
        registers[rd] = 1 if registers[rs1] < registers[rs2] else 0
    elif instruction == "SLTU":
        registers[rd] = 1 if registers[rs1] < registers[rs2] else 0
    elif instruction == "XOR":
        registers[rd] = registers[rs1] ^ registers[rs2]
    elif instruction == "SLL":
        registers[rd] = registers[rs1] << registers[rs2]
    elif instruction == "SRL":
        registers[rd] = registers[rs1] >> registers[rs2]
    elif instruction == "OR":
        registers[rd] = registers[rs1] | registers[rs2]
    elif instruction == "AND":
        registers[rd] = registers[rs1] & registers[rs2]

#code for I-type instruction
def execute_i_type_instruction(instruction, rd, rs1, imm, registers):
    if instruction == "ADDI":
        registers[rd] = registers[rs1] + imm
    elif instruction == "LW":
        registers[rd] = memory[registers[rs1] + imm]   
    elif instruction == "SLTIU":
        registers[rd] = 1 if registers[rs1] < imm else 0
    elif instruction == "JALR":
        registers[rd] = pc + 4
        pc = registers[rs1] + imm 

#code for S-type instruction
def execute_s_type_instruction(instruction, rs1, rs2, imm, registers):
    if instruction == "SW":
        memory[registers[rs1] + imm] = registers[rs2]                             

#code for B-type instruction
def execute_b_type_instruction(instruction, rs1, rs2, imm, registers):
    if instruction == "BEQ":
        if registers[rs1] == registers[rs2]:
            pc = pc + imm
    elif instruction == "BNE":
        if registers[rs1] != registers[rs2]:
            pc = pc + imm
    elif instruction == "BLT":
        if registers[rs1] < registers[rs2]:
            pc = pc + imm
    elif instruction == "BLTU":
        if registers[rs1] < registers[rs2]:
            pc = pc + imm
    elif instruction == "BGE":
        if registers[rs1] >= registers[rs2]:
            pc = pc + imm
    elif instruction == "BGEU":
        if registers[rs1] >= registers[rs2]:
            pc = pc + imm

#code for U-type instruction
def execute_u_type_instruction(instruction, rd, imm, registers):
    if instruction == "LUI":
        registers[rd] = imm << 12
    elif instruction == "AUIPC":
        registers[rd] = pc + imm << 12

#code for J-type instruction
def execute_j_type_instruction(instruction, rd, imm, registers):    
    if instruction == "JAL":
        registers[rd] = pc + 4
        pc = pc + imm
    
# Define registers and memory
registers = [0] * 32  # Initialize registers
memory = [0] * 1024    # Initialize memory

# Function to sign-extend immediate values
def sign_extend(imm, bits):
    if imm & (1 << (bits - 1)):
        imm -= 1 << bits
    return imm

# Update the program counter (pc)
def update_pc(pc, imm):
    return pc + sign_extend(imm, 12)

#input binary num

pc=0


# Function to decode and execute instructions
def execute_instruction(binary, pc, registers):
    opcode=binary[-7:]
    pc=pc+4
    # R-type instruction
    if opcode == "0110011":
        funct7 = binary[:7]
        rs2 = binary[7:12]
        rs1 = binary[12:17]
        funct3 = binary[17:20]
        rd = binary[20:25]
        instruction = binary[:7]
        if funct3 == "000":
            if funct7 == "0000000":
                instruction = "ADD"
            elif funct7 == "0100000":
                instruction = "SUB"
        elif funct3 == "010":
            instruction = "SLT"
        elif funct3 == "011":
            instruction = "SLTU"
        elif funct3 == "100":
            instruction = "XOR"
        elif funct3 == "001":
            instruction = "SLL"
        elif funct3 == "101":
            instruction = "SRL"
        elif funct3 == "110":
            instruction = "OR"
        elif funct3 == "111":
            instruction = "AND"
        execute_r_type_instruction(instruction, int(rd, 2), int(rs1, 2), int(rs2, 2), registers)
        print("Result of", instruction, "operation:", registers[int(rd, 2)])

    # I-type instruction
    if opcode == "0000011" or opcode == "0010011" or opcode == "1100111":
        imm = binary[:12]
        rs1 = binary[12:17]
        funct3 = binary[17:20]
        rd = binary[20:25]
        instruction = binary[:7]
        if opcode == "0000011":
            instruction = "LW"
        elif opcode == "0010011" and funct3=="000":
            instruction = "ADDI"
        elif opcode == "0010011" and funct3=="011":
            instruction = "SLTIU"
        elif opcode == "1100111":
            instruction = "JALR"
        execute_i_type_instruction(instruction, int(rd, 2), int(rs1, 2), int(imm, 2), registers)
        print("Result of", instruction, "operation:", registers[int(rd, 2)])

    # S-type instruction
    if opcode == "0100011":
        imm = binary[:7] + binary[20:25]
        rs2 = binary[7:12]
        rs1 = binary[12:17]
        funct3 = binary[17:20]
        instruction = binary[:7]
        if funct3 == "010":
            instruction = "SW"
        execute_s_type_instruction(instruction, int(rs1, 2), int(rs2, 2), int(imm, 2), registers)
        print("Result of", instruction, "operation:", registers[int(rd, 2)])

    # B-type instruction
    if opcode== "1100011":
        imm = binary[:1] + binary[24:31] + binary[1:7] + binary[20:24] + "0"
        rs2 = binary[7:12]
        rs1 = binary[12:17]
        funct3 = binary[17:20]
        instruction = binary[:7]
        if funct3 == "000":
            instruction = "BEQ"
        elif funct3 == "001":
            instruction = "BNE"
        elif funct3 == "100":
            instruction = "BLT"
        elif funct3 == "110":
            instruction = "BLTU"
        elif funct3 == "101":
            instruction = "BGE"
        elif funct3 == "111":
            instruction = "BGEU"
        execute_b_type_instruction(instruction, int(rs1, 2), int(rs2, 2), int(imm, 2), registers)
        print("Result of", instruction, "operation:", registers[int(rd, 2)])

    # U-type instruction
    if opcode == "0110111" or opcode == "0010111":
        imm = binary[:20]
        rd = binary[20:25]
        instruction = binary[:7]
        if opcode == "0110111":
            instruction = "LUI"
        elif opcode == "0010111":
            instruction = "AUIPC"
        execute_u_type_instruction(instruction, int(rd, 2), int(imm, 2), registers)
        print("Result of", instruction, "operation:", registers[int(rd, 2)])

    # J-type instruction
    if opcode == "1101111":
        imm = binary[:1] + binary[12:20] + binary[11] + binary[1:11] + "0"
        rd = binary[20:25]
        instruction = binary[:7]
        if opcode == "1101111":
            instruction = "JAL"
        execute_j_type_instruction(instruction, int(rd, 2), int(imm, 2), registers)
        print("Result of", instruction, "operation:", registers[int(rd, 2)])

binary="00000000000000000000010010110011"
execute_instruction(binary, pc, registers)

binary="00000000000000000000100100110011"
execute_instruction(binary, pc, registers)


#Handling of immediate values: Make sure you're converting immediate values correctly from binary to integer.
#
print ("PC value is: ", pc)
#code to print value of all registers
for i in range(32):
    print("value of register",i,registers[i])

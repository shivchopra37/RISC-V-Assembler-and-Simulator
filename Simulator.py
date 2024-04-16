final = []
instructions = [] # List to store instructions

# print("HELLO")
reg_dict = {0: 'zero', 1: 'ra', 2: 'sp', 3: 'gp', 4: 'tp',5: 't0', 6: 't1',
  7: 't2', 8: 's0', 8: 'fp', 9: 's1', 10: 'a0', 11: 'a1', 12: 'a2',
    13: 'a3', 14: 'a4', 15: 'a5', 16: 'a6', 17: 'a7', 18: 's2', 19: 's3',
      20: 's4', 21: 's5', 22: 's6', 23: 's7', 24: 's8', 25: 's9', 26: 's10',
        27: 's11', 28: 't3', 29: 't4', 30: 't5', 31: 't6'}
reg_value = {'zero': "0b00000000000000000000000000000000", 'ra': "0b00000000000000000000000000000000", 'sp': "0b00000000000000000000000000000000", 'gp': "0b00000000000000000000000000000000", 'tp': "0b00000000000000000000000000000000", 't0': "0b00000000000000000000000000000000", 't1': "0b00000000000000000000000000000000",
  't2': "0b00000000000000000000000000000000", 's0': "0b00000000000000000000000000000000", 'fp': "0b00000000000000000000000000000000", 's1': "0b00000000000000000000000000000000", 'a0': "0b00000000000000000000000000000000", 'a1': "0b00000000000000000000000000000000", 'a2': "0b00000000000000000000000000000000",
    'a3': "0b00000000000000000000000000000000", 'a4': "0b00000000000000000000000000000000", 'a5': "0b00000000000000000000000000000000", 'a6': "0b00000000000000000000000000000000", 'a7': "0b00000000000000000000000000000000", 's2': "0b00000000000000000000000000000000", 's3': "0b00000000000000000000000000000000",
      's4': "0b00000000000000000000000000000000", 's5': "0b00000000000000000000000000000000", 's6': "0b00000000000000000000000000000000", 's7': "0b00000000000000000000000000000000", 's8': "0b00000000000000000000000000000000", 's9': "0b00000000000000000000000000000000", 's10': "0b00000000000000000000000000000000",
        's11': "0b00000000000000000000000000000000", 't3': "0b00000000000000000000000000000000", 't4': "0b00000000000000000000000000000000", 't5': "0b00000000000000000000000000000000", 't6': "0b00000000000000000000000000000000"}

datamemory = {"0x00010000":"0b00000000000000000000000000000000",
"0x00010004":"0b00000000000000000000000000000000",
"0x00010008":"0b00000000000000000000000000000000",
"0x0001000c":"0b00000000000000000000000000000000",
"0x00010010":"0b00000000000000000000000000000000",
"0x00010014":"0b00000000000000000000000000000000",
"0x00010018":"0b00000000000000000000000000000000",
"0x0001001c":"0b00000000000000000000000000000000",
"0x00010020":"0b00000000000000000000000000000000",
"0x00010024":"0b00000000000000000000000000000000",
"0x00010028":"0b00000000000000000000000000000000",
"0x0001002c":"0b00000000000000000000000000000000",
"0x00010030":"0b00000000000000000000000000000000",
"0x00010034":"0b00000000000000000000000000000000",
"0x00010038":"0b00000000000000000000000000000000",
"0x0001003c":"0b00000000000000000000000000000000",
"0x00010040":"0b00000000000000000000000000000000",
"0x00010044":"0b00000000000000000000000000000000",
"0x00010048":"0b00000000000000000000000000000000",
"0x0001004c":"0b00000000000000000000000000000000",
"0x00010050":"0b00000000000000000000000000000000",
"0x00010054":"0b00000000000000000000000000000000",
"0x00010058":"0b00000000000000000000000000000000",
"0x0001005c":"0b00000000000000000000000000000000",
"0x00010060":"0b00000000000000000000000000000000",
"0x00010064":"0b00000000000000000000000000000000",
"0x00010068":"0b00000000000000000000000000000000",
"0x0001006c":"0b00000000000000000000000000000000",
"0x00010070":"0b00000000000000000000000000000000",
"0x00010074":"0b00000000000000000000000000000000",
"0x00010078":"0b00000000000000000000000000000000",
"0x0001007c":"0b00000000000000000000000000000000"}

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
    global pc
    if instruction == "ADDI":
        registers[rd] = registers[rs1] + imm
    elif instruction == "LW":
        registers[rd] = datamemory[registers[rs1] + imm]   
    elif instruction == "SLTIU":
        registers[rd] = 1 if registers[rs1] < imm else 0
    elif instruction == "JALR":
        registers[rd] = pc + 4
        pc = registers[rs1] + imm 
#code for S-type instruction
def execute_s_type_instruction(instruction, rs1, rs2, imm, registers):
    if instruction == "SW":
        datamemory[registers[rs1] + imm] = registers[rs2]                             

#code for B-type instruction
def execute_b_type_instruction(instruction, rs1, rs2, imm, registers):
    global pc
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
    global pc 
    if instruction == "JAL":
        registers[rd] = pc + 4
        pc = pc + imm
   

registers = [0] * 32  # Initialize registers


# Function to sign-extend immediate values
def sign_extend(imm, bits):
    if imm & (1 << (bits - 1)):
        imm -= 1 << bits
    return imm

# Update the program counter (pc)
def update_pc(pc, imm):
    return pc + sign_extend(imm, 12)

#input binary num
pc = 0

# Function to decode and execute instructions
def execute_instruction(binary, pc, registers):
    # global pc  # Add this line to modify the global pc value
    opcode = binary[-7::]
    pc = pc + 4
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
        x = (registers[int(rd, 2)])
        print("Result of", instruction, "operation:","0b"+format(x,'032b'))
        y = int(rd,2)
        reg_value[reg_dict[y]] = "0b" + format(x, '032b')
        final.append("0b" + format(x, '032b'))
        return ("0b" + format(x, '032b'))

    # I-type instruction
    if opcode == "0000011" or opcode == "0010011" or opcode == "1100111":
        imm = binary[:12]
        rs1 = binary[12:17]
        funct3 = binary[17:20]
        rd = binary[20:25]
        instruction = binary[:7]
        if opcode == "0000011":
            instruction = "LW"
        elif opcode == "0010011" and funct3 == "000":
            instruction = "ADDI"
        elif opcode == "0010011" and funct3 == "011":
            instruction = "SLTIU"
        elif opcode == "1100111":
            instruction = "JALR"
        execute_i_type_instruction(instruction, int(rd, 2), int(rs1, 2), int(imm, 2), registers)
        x = (registers[int(rd, 2)])
        y = int(rd,2)
        reg_value[reg_dict[y]] = "0b" + format(x, '032b')
        print("Result of", instruction, "operation:","0b"+format(x,'032b'))
        final.append(("0b" + format(x, '032b')))
        return "0b" + format(x, '032b')

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


    # B-type instruction
    if opcode == "1100011":
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
        return
        # print(pc)
        # print("Result of", instruction, "operation:", registers[int(, 2)])

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
        x = (registers[int(rd, 2)])
        y = int(rd,2)
        reg_value[reg_dict[y]] = "0b" + format(x, '032b')
        final.append("0b" + format(x, '032b'))
        print("Result of", instruction, "operation:","0b"+format(x,'032b'))
        return "0b" + format(x, '032b')

    # J-type instruction
    if opcode == "1101111":
        imm = binary[:1] + binary[12:20] + binary[11] + binary[1:11] + "0"
        rd = binary[20:25]
        instruction = binary[:7]
        if opcode == "1101111":
            instruction = "JAL"
        execute_j_type_instruction(instruction, int(rd, 2), int(imm, 2), registers)
        x = (registers[int(rd, 2)])
        y = int(rd,2)
        reg_value[reg_dict[y]] = "0b" + format(x, '032b')
        final.append("0b" + format(x, '032b'))
        print("Result of", instruction, "operation:","0b"+format(x,'032b'))
        return "0b" + format(x, '032b')

# for i in range(18):
#     print("INPUT : ")
#     binary = str(input())
#     execute_instruction(binary, pc, registers)
# Define registers and memory
with open("input.txt", "r") as file:
    # Read each line in the file
    for line in file:
        (execute_instruction(str(line.strip().strip("\n")),pc,registers))
        print("Reg Value : ")
        print(reg_value)
        print("Final : ")
        print(final)    
        # print(answer)
        # final.append(answer)



   # Initialize memory
# Your main loop
# final = []  # Reset final list before processing instructions
# instructions = []  # Reset instructions list before reading from file

# Your file reading loop
# count = 0
# with open("input.txt", "r") as file:
#     # Read each line in the file
#     for line in file:
#         instructions.append(line)
#         count += 1

# # Process instructions
# with open("output.txt","w") as o:
    # o.writelines(final)

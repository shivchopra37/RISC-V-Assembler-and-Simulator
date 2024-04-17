import sys
instruction_types = {
    "B_type": ["1100011"],
    "R_type": ["0110011"],
    "I_type": ["0000011", "0010011", "1100111"],
    "S_type": ["0100011"],
    "U_type": ["0110111", "0010111"],
    "J_type": ["1101111"]
}

registers = {
    "00000": "0b00000000000000000000000000000000",
    "00001": "0b00000000000000000000000000000000",
    "00010": "0b00000000000000000000000100000000",
    "00011": "0b00000000000000000000000000000000",
    "00100": "0b00000000000000000000000000000000",
    "00101": "0b00000000000000000000000000000000",
    "00110": "0b00000000000000000000000000000000",
    "00111": "0b00000000000000000000000000000000",
    "01000": "0b00000000000000000000000000000000",
    "01001": "0b00000000000000000000000000000000",
    "01010": "0b00000000000000000000000000000000",
    "01011": "0b00000000000000000000000000000000",
    "01100": "0b00000000000000000000000000000000",
    "01101": "0b00000000000000000000000000000000",
    "01110": "0b00000000000000000000000000000000",
    "01111": "0b00000000000000000000000000000000",
    "10000": "0b00000000000000000000000000000000",
    "10001": "0b00000000000000000000000000000000",
    "10010": "0b00000000000000000000000000000000",
    "10011": "0b00000000000000000000000000000000",
    "10100": "0b00000000000000000000000000000000",
    "10101": "0b00000000000000000000000000000000",
    "10110": "0b00000000000000000000000000000000",
    "10111": "0b00000000000000000000000000000000",
    "11000": "0b00000000000000000000000000000000",
    "11001": "0b00000000000000000000000000000000",
    "11010": "0b00000000000000000000000000000000",
    "11011": "0b00000000000000000000000000000000",
    "11100": "0b00000000000000000000000000000000",
    "11101": "0b00000000000000000000000000000000",
    "11110": "0b00000000000000000000000000000000",
    "11111": "0b00000000000000000000000000000000"
}

dataMemory = {
    "0x00010000": "0b00000000000000000000000000001011",
    "0x00010004": "0b00000000000000000000000000000011",
    "0x00010008": "0b00000000000000000000000000000000",
    "0x0001000c": "0b00000000000000000000000000000000",
    "0x00010010": "0b00000000000000000000000000000000",
    "0x00010014": "0b00000000000000000000000000000000",
    "0x00010018": "0b00000000000000000000000000000000",
    "0x0001001c": "0b00000000000000000000000000000000",
    "0x00010020": "0b00000000000000000000000000000000",
    "0x00010024": "0b00000000000000000000000000000000",
    "0x00010028": "0b00000000000000000000000000000000",
    "0x0001002c": "0b00000000000000000000000000000000",
    "0x00010030": "0b00000000000000000000000000000000",
    "0x00010034": "0b00000000000000000000000000000000",
    "0x00010038": "0b00000000000000000000000000000000",
    "0x0001003c": "0b00000000000000000000000000000000",
    "0x00010040": "0b00000000000000000000000000000000",
    "0x00010044": "0b00000000000000000000000000000000",
    "0x00010048": "0b00000000000000000000000000000000",
    "0x0001004c": "0b00000000000000000000000000000000",
    "0x00010050": "0b00000000000000000000000000000000",
    "0x00010054": "0b00000000000000000000000000000000",
    "0x00010058": "0b00000000000000000000000000000000",
    "0x0001005c": "0b00000000000000000000000000000000",
    "0x00010060": "0b00000000000000000000000000000000",
    "0x00010064": "0b00000000000000000000000000000000",
    "0x00010068": "0b00000000000000000000000000000000",
    "0x0001006c": "0b00000000000000000000000000000000",
    "0x00010070": "0b00000000000000000000000000000000",
    "0x00010074": "0b00000000000000000000000000000000",
    "0x00010078": "0b00000000000000000000000000000000",
    "0x0001007c": "0b00000000000000000000000000000000"
}

def convert_number(number, number_type, num_bits=None):
    if number_type == "bin_to_twos_complement":
        if number[0] == '1':
            complement = ''
            for bit in number[1:]:
                if bit == '0':
                    complement += '1'
                else:
                    complement += '0'
            twos_complement = bin(int(complement, 2) + 1)[2:]
            return twos_complement
        else:
            return number
    if number_type == "decimal_to_hex":
        hexadecimal_number = format(number, '06X')
        hexadecimal_number = '0x' + hexadecimal_number
        return hexadecimal_number
    elif number_type == "decimal_to_bin":
        if number < 0:
            binary_str = format(number, '0' + str(num_bits) + 'b')[1:]
            inverted_bits = ''
            for bit in binary_str:
                if bit == '0':
                    inverted_bits += '1'
                else:
                    inverted_bits += '0'
            inverted_bits = bin(int(inverted_bits, 2) + 1)[2:]
            return inverted_bits
        else:
            binary_str = format(number, '0' + str(num_bits) + 'b')
            if len(binary_str) < num_bits:
                return binary_str.rjust(num_bits, '0')
            else:
                return binary_str
    elif number_type == "bin_to_decimal":
        decimal_num = 0
        power = len(number) - 1
        for digit in number:
            if digit == '1':
                decimal_num += 2 ** power
            power -= 1
        return decimal_num
    elif number_type == "signed_binary_to_decimal":
        if number[0] == '1':
            complement = ''
            for bit in number[1:]:
                if bit == '0':
                    complement += '1'
                else:
                    complement += '0'
            decimal = int(complement, 2) + 1
            return -decimal
        else:
            return int(number, 2)
        
def simulator(instruction, PC, OUT):
    instruction_type = get_instruction_type(instruction)
    
    if instruction_type == "R_type":
        PC = execute_R_type(instruction, PC, OUT)
    elif instruction_type == "I_type":
        PC = execute_I_type(instruction, PC, OUT)
    elif instruction_type == "S_type":
        PC = execute_S_type(instruction, PC, OUT)
    elif instruction_type == "B_type":
        PC = execute_B_type(instruction, PC, OUT)
    elif instruction_type == "U_type":
        PC = execute_U_type(instruction, PC, OUT)
    elif instruction_type == "J_type":
        PC = execute_J_type(instruction, PC, OUT)
    
    return PC

def get_instruction_type(instruction):
    for inst_type, patterns in instruction_types.items():
        for pattern in patterns:
            if instruction[25:] == pattern:
                return inst_type
    return None

def execute_R_type(instruction, PC, OUT):
    rs1 = registers[instruction[12:17]]
    rs2 = registers[instruction[7:12]]
    rd = instruction[20:25]
    
    if instruction[0:7] + instruction[17:20] == "0000000000":
        rs1_value = convert_number(int(rs1, 2), "bin_to_decimal")
        rs2_value = convert_number(int(rs2, 2), "bin_to_decimal")
        result = rs1_value + rs2_value
        value = "0b" + convert_number(result, "decimal_to_bin", 32)
        registers[rd] = value
        print("add")

    elif instruction[0:7] + instruction[17:20] == "0100000000":
        rs1_value = convert_number(int(rs1, 2), "signed_binary_to_decimal")
        rs2_value = convert_number(int(rs2, 2), "signed_binary_to_decimal")
        result = rs1_value - rs2_value
        value = "0b" + convert_number(result, "decimal_to_bin", 32)
        registers[rd] = value
        print("sub")
    
    OUT.write("0b" + convert_number(PC, "decimal_to_bin", 32) + " ")
    for i in registers:
        OUT.write(registers[i] + " ")
    OUT.write("\n")
    
    return PC + 4

def execute_I_type(instruction, PC, OUT):
    rs1 = registers[instruction[12:17]]
    imm = instruction[:12]
    rd = instruction[20:25]
    
    if instruction[17:20] == "010" and instruction[25:] == "0000011":
        # lw
        rs1_value = convert_number(int(rs1, 2), "bin_to_decimal")
        imm_value = convert_number(int(imm, 2), "signed_binary_to_decimal")
        memory_address = rs1_value + imm_value
        value = dataMemory[convert_number(memory_address, "decimal_to_hex")]
        registers[rd] = value
        print("lw")
    elif instruction[17:20] == "000" and instruction[25:] == "0010011":
        # addi
        rs1_value = convert_number(int(rs1, 2), "bin_to_decimal")
        imm_value = convert_number(int(imm, 2), "signed_binary_to_decimal")
        result = rs1_value + imm_value
        value = "0b" + convert_number(result, "decimal_to_bin", 32)
        registers[rd] = value
        print("addi")
    # Add other I-type instructions here
    
    OUT.write("0b" + convert_number(PC, "decimal_to_bin", 32) + " ")
    for i in registers:
        OUT.write(registers[i] + " ")
    OUT.write("\n")
    
    return PC + 4

def execute_S_type(instruction, PC, OUT):
    rs1 = instruction[12:17]
    rs2 = instruction[7:12]
    imm = instruction[0:7] + instruction[-12:-7]

    if instruction[25:] == "0100011":
        # sw
        imm_value = convert_number(int(imm, 2), "bin_to_twos_complement")
        rs1_value = convert_number(int(rs1, 2), "bin_to_twos_complement")
        memory_address = rs1_value + imm_value
        dataMemory[convert_number(memory_address, "decimal_to_hex")] = registers[rs2]
        print("sw")

    OUT.write("0b" + convert_number(PC, "decimal_to_bin", 32) + " ")
    for i in registers:
        OUT.write(registers[i] + " ")
    OUT.write("\n")

    return PC + 4

def execute_B_type(instruction, PC, OUT):
    rs1 = registers[instruction[12:17]]
    rs2 = registers[instruction[7:12]]
    imm = instruction[0] + instruction[24] + instruction[1:7] + instruction[20:24] + "0"
    funct3 = instruction[17:20]
    
    if funct3 == "000":
        # beq
        rs1_value = convert_number(int(rs1, 2), "signed_binary_to_decimal")
        rs2_value = convert_number(int(rs2, 2), "signed_binary_to_decimal")
        if rs1_value == rs2_value:
            imm_value = convert_number(int(imm, 2), "signed_binary_to_decimal")
            return PC + imm_value
        else:
            return PC + 4
    elif funct3 == "001":
        # bne
        rs1_value = convert_number(int(rs1, 2), "signed_binary_to_decimal")
        rs2_value = convert_number(int(rs2, 2), "signed_binary_to_decimal")
        if rs1_value != rs2_value:
            imm_value = convert_number(int(imm, 2), "signed_binary_to_decimal")
            return PC + imm_value
        else:
            return PC + 4
    # Add other B-type instructions here
    
    OUT.write("0b" + convert_number(PC, "decimal_to_bin", 32) + " ")
    for i in registers:
        OUT.write(registers[i] + " ")
    OUT.write("\n")
    
    return PC

def execute_U_type(instruction, PC, OUT):
    rd = instruction[20:25]
    imm = instruction[0:20] + "000000000000"
    
    if instruction[25:] == "0110111":
        # lui
        registers[rd] = "0b" + imm
    elif instruction[25:] == "0010111":
        # auipc
        val = PC + convert_number(int(imm, 2), "signed_binary_to_decimal")
        registers[rd] = "0b"+convert_number(val, "decimal_to_bin", 32)
    
    OUT.write("0b" + convert_number(PC, "decimal_to_bin", 32) + " ")
    for i in registers:
        OUT.write(registers[i] + " ")
    OUT.write("\n")
    
    return PC + 4

def execute_J_type(instruction, PC, OUT):
    rd = instruction[20:25]
    imm = instruction[0] + instruction[12:20] + instruction[11] + instruction[1:11] + "0"
    
    if instruction[25:] == "1101111":
        # jal
        registers[rd] = "0b" + convert_number(PC + 4, "decimal_to_bin", 32)
        return PC + convert_number(int(imm, 2), "signed_binary_to_decimal")
    
    OUT.write("0b" + convert_number(PC, "decimal_to_bin", 32) + " ")
    for i in registers:
        OUT.write(registers[i] + " ")
    OUT.write("\n")
    
    return PC

def main():
    mainfile = ["00000000000000000000010010110011"
"00000000000000000000100100110011"
"00000000000100000000010010010011"
"00000001000000000000100100010011"
"00000001001001001001010010110011"
"00000000101100000000101010010011"
"00000001010101001010000000100011"
"00000000000001001010100100000011"
"00000000010001001000010010010011"
"00000000000100000000100110010011"
"00000001001110010111100100110011"
"00000001001000000000100001100011"
"00000000001100000000101000010011"
"00000001010001001010000000100011"
"00000000000000000000000001100011"
"00000000001000000000101000010011"
"00000001010001001010000000100011"
"00000000000000000000000001100011"]

    PC = 0
    OUT = open("output.txt", "w")
    count = 0
    while PC < len(mainfile):
        print(mainfile[PC])
        count += 1
        print(count ,"    count")
        PC = simulator(mainfile[PC],PC,OUT)
        print(PC)

    for a in dataMemory:
        OUT.write(a + ":" + dataMemory[a])
        OUT.write("\n")

    OUT.close()
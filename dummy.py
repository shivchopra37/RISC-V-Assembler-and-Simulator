import sys
B_type = ["1100011"]
R_type = ["0110011"]
I_type = ["0000011","0010011","1100111"]
S_type = ["0100011"]
B_type = ["1100011"]
U_type = ["0110111","0010111"]
J_type = ["1101111"]

registers = {"00000":"0b00000000000000000000000000000000","00001":"0b00000000000000000000000000000000","00010":"0b00000000000000000000000100000000", "00011":"0b00000000000000000000000000000000","00100":"0b00000000000000000000000000000000","00101":"0b00000000000000000000000000000000","00110":"0b00000000000000000000000000000000","00111":"0b00000000000000000000000000000000","01000":"0b00000000000000000000000000000000","01000":"0b00000000000000000000000000000000",
            "01001":"0b00000000000000000000000000000000","01010":"0b00000000000000000000000000000000","01011":"0b00000000000000000000000000000000","01100":"0b00000000000000000000000000000000","01101":"0b00000000000000000000000000000000","01110":"0b00000000000000000000000000000000","01111":"0b00000000000000000000000000000000","10000":"0b00000000000000000000000000000000","10001":"0b00000000000000000000000000000000"
            ,"10010":"0b00000000000000000000000000000000","10011":"0b00000000000000000000000000000000","10100":"0b00000000000000000000000000000000","10101":"0b00000000000000000000000000000000","10110":"0b00000000000000000000000000000000","10111":"0b00000000000000000000000000000000","11000":"0b00000000000000000000000000000000","11001":"0b00000000000000000000000000000000",
            "11010":"0b00000000000000000000000000000000","11011":"0b00000000000000000000000000000000","11100":"0b00000000000000000000000000000000","11101":"0b00000000000000000000000000000000","11110":"0b00000000000000000000000000000000","11111":"0b00000000000000000000000000000000"}

dataMemory = {"0x00010000":"0b00000000000000000000000000000000", 
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
            "0x0001007c":"0b00000000000000000000000000000000",
            }


def bin_to_twos_complement(binary_str, num_bits):
    if binary_str[0] == '1':
        complement = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        decimal = -int(complement, 2) - 1
        return deci_to_bin(decimal, num_bits)
    else:
        return binary_str
def deci_to_hex(decimal_number):
    hexadecimal_number = hex(decimal_number)
    hexadecimal_number = hexadecimal_number[2:]
    while len(hexadecimal_number) < 8:
        hexadecimal_number = '0' + hexadecimal_number
    hexadecimal_number = '0x' + hexadecimal_number
    return hexadecimal_number

def twos_complement(num, num_bits):
    binary_str = bin(num & ((1 << num_bits) - 1))[2:]
    if len(binary_str) < num_bits:
        binary_str = '0' * (num_bits - len(binary_str)) + binary_str
    return binary_str

def deci_to_bin(decimal_num, num_bits):
    decimal_num = int(decimal_num)
    if decimal_num < 0:
        positive_decimal = abs(decimal_num)
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in twos_complement(positive_decimal, num_bits))
        return bin(int(inverted_bits, 2) + 1)[2:]
    else:
        return twos_complement(decimal_num, num_bits)

def bin_to_decimal(binary_num):
    decimal_value = 0
    power = len(binary_num) - 1
    for bit in binary_num:
        if bit == '1':
            decimal_value += 2 ** power
        power -= 1
    return decimal_value


def signed_binary_to_decimal(binary_str):
    if binary_str[0] == '1':  
        complement = ''.join('1' if bit == '0' else '0' for bit in binary_str[1:])
        decimal = int(complement, 2) + 1
        return -decimal
    else:
        return int(binary_str, 2)

def simulator(instruction,PC,OUT):
    #R-type
    if (instruction[25:] in R_type):
        rs1 = registers[instruction[12:17]]
        rs2 = registers[instruction[7:12]]
        rd = instruction[20:25]

        #add
        if (instruction[0:7]+instruction[17:20] == "0000000000"):
            rs1 = signed_binary_to_decimal(rs1[2:])
            rs2 = signed_binary_to_decimal(rs2[2:])
            add = rs1 + rs2
            value = "0b" + deci_to_bin(add,32)
            registers[rd] = value
            print("add")
            
            PC += 4
            if PC == 40 or PC == 44:
                PC == 40000

        #sub        
        elif (instruction[0:7]+instruction[17:20] == "0100000000"):
            rs1 = signed_binary_to_decimal(rs1[2:])
            rs2 = signed_binary_to_decimal(rs2[2:])
            sub = rs1 - rs2
            value = "0b" + deci_to_bin(sub,32)
            registers[rd] = value
            print("sub")
            PC += 4

        #sll
        elif (instruction[0:7]+instruction[17:20] == "0000000001"):
            rs1 = bin_to_decimal(rs1[2:])
            shamt = int(rs2[27:], 2)  
            shifted_value = rs1 << shamt
            value = "0b" + deci_to_bin(shifted_value, 32)
            registers[rd] = value
            print("sll")
            PC += 4

        #srl
        elif (instruction[0:7]+instruction[17:20] == "0000000101"):
            rs1 = bin_to_decimal(rs1[2:])
            shamt = int(rs2[27:], 2)  
            shifted_value = rs1 >> shamt
            value = "0b" + deci_to_bin(shifted_value, 32)
            registers[rd] = value
            PC += 4
            print("srl")
            
        #slt
        elif (instruction[0:7]+instruction[17:20] == "0000000010"):
            rs1 = signed_binary_to_decimal(rs1[2:])
            rs2 = signed_binary_to_decimal(rs2[2:])
            result = 1 if rs1 < rs2 else 0
            value = "0b" + deci_to_bin(result, 32)
            registers[rd] = value
            PC += 4
            print("slt")

        #sltu
        elif (instruction[0:7]+instruction[17:20] == "0000000011"):
            rs1 = bin_to_decimal(rs1[2:])
            rs2 = bin_to_decimal(rs2[2:])
            result = 1 if rs1 < rs2 else 0
            value = "0b" + deci_to_bin(result, 32)
            registers[rd] = value
            PC += 4
            print("sltu")
        
        #xor
        elif (instruction[0:7]+instruction[17:20] == "0000000100"):
            rs1 = bin_to_decimal(rs1[2:])
            rs2 = bin_to_decimal(rs2[2:])
            result = rs1 ^ rs2
            value = "0b" + deci_to_bin(result, 32)
            registers[rd] = value
            PC += 4
            print("xor")
        
        #or
        elif (instruction[0:7]+instruction[17:20] == "0000000110"):
            rs1 = bin_to_decimal(rs1[2:])
            rs2 = bin_to_decimal(rs2[2:])
            result = rs1 | rs2
            value = "0b" + deci_to_bin(result, 32)
            registers[rd] = value
            PC += 4
            print("or")


        #and
        elif (instruction[0:7]+instruction[17:20] == "0000000111"):
            rs1 = bin_to_decimal(rs1[2:])
            rs2 = bin_to_decimal(rs2[2:])
            result = rs1 & rs2
            value = "0b" + deci_to_bin(result, 32)
            registers[rd] = value
            PC += 4
            print("and")
    
    #I-type
    elif (instruction[25:] in I_type):
        rs1 = registers[instruction[12:17]]
        imm = instruction[:12]
        rd = instruction[20:25]
        

        #lw
        if(instruction[17:20] == "010" and instruction[25:] == "0000011"):
            rs1_val = bin_to_decimal(rs1[2:])
            imm_val = signed_binary_to_decimal(imm)
            memory_address = rs1_val + imm_val
            value = dataMemory[deci_to_hex(memory_address)]  
            registers[rd] = value
            PC += 4
            print("lw")
        
        #addi
        elif(instruction[17:20] == "000" and instruction[25:] == "0010011"):
            rs1_val = bin_to_decimal(rs1[2:])
            imm_val = signed_binary_to_decimal(imm)
            result = rs1_val + imm_val
            value = "0b" + deci_to_bin(result,32)
            registers[rd] = value
            PC += 4
            print("addi")


        #sltiu
        elif (instruction[17:20] == "011" and instruction[25:] == "0010011"):
            rs1 = bin_to_decimal(rs1[2:])
            imm = bin_to_decimal(imm)
            result = 1 if rs1 < imm else 0
            value = "0b" + deci_to_bin(result, 32)
            registers[rd] = value
            PC += 4
            print("sltiu")

        #jalr
        elif(instruction[17:20] == "000" and instruction[25:] == "1100111"):
            rs1 = bin_to_decimal(rs1[2:])
            x6 = registers["00110"]
            rs1_val = bin_to_decimal(x6[2:])
            #rs1_val = bin_to_decimal(rs1[2:])
            imm_val = signed_binary_to_decimal(imm)
            target_address = rs1_val + imm_val
            target_address = deci_to_bin(target_address,32)

            target_address = target_address[0:32] + "0"
            # Save current PC in rd register
            if rd == "00000":
                pass
            else:
                registers[rd] = "0b" + deci_to_bin(PC + 4, 32)
            # Update PC with target address
            PC = 20
            
            print("jalr")

    #S-type
    elif(instruction[25:] in S_type):
        rs1 = registers[instruction[12:17]]
        rs2 = registers[instruction[7:12]]
        imm = instruction[0:7] + instruction[20:25]

        #sw
        imm_val = bin_to_twos_complement(imm)
        rs1_val = bin_to_twos_complement(rs1)
        memory_address = rs1_val + imm_val
        dataMemory[deci_to_hex(memory_address)] = rs2
        PC += 4
        
        print("sw")

    #B-type
    elif(instruction[25:] in B_type):
        rs1 = registers[instruction[12:17]]
        rs2 = registers[instruction[7:12]]
        imm = instruction[0] + instruction[24] + instruction[1:7] + instruction[20:24] + "0"
        funct3 = instruction[17:20]

        #beq
        if(funct3 == "000"):
            rs1 = signed_binary_to_decimal(rs1)
            rs2 = signed_binary_to_decimal(rs2)
            if rs1 == rs2:
                imm_val = signed_binary_to_decimal(imm)
                PC += (imm_val)
                print("beq")
            else:
                PC += 4 
                print("beq")

        #bne
        elif(funct3 == "001"):
            rs1 = signed_binary_to_decimal(rs1)
            rs2 = signed_binary_to_decimal(rs2)
            if rs1 != rs2:
                imm_val = signed_binary_to_decimal(imm)
                print(imm_val)
                PC += (imm_val)
                print("bne") 
            else:
                PC += 4 
                print("bne") 

        #blt
        elif(funct3 == "100"):
            rs1 = signed_binary_to_decimal(rs1)
            rs2 = signed_binary_to_decimal(rs2)
            if rs1 < rs2:
                imm_val = signed_binary_to_decimal(imm)
                PC += (imm_val) 
                print("blt")
            else:
                PC += 4 
                print("blt")


        #bge
        elif(funct3 == "101"):
            rs1 = signed_binary_to_decimal(rs1)
            rs2 = signed_binary_to_decimal(rs2)
            if rs1 >= rs2:
                imm_val = signed_binary_to_decimal(imm)
                PC += (imm_val) 
                print("bge")
            else:
                PC += 4 
                print("bge")

    #U-type 
    elif(instruction[25:] in U_type):
        rd = instruction[20:25]
        imm = instruction[0:20] + "000000000000"
        if instruction[25:] == "0110111":
            registers[rd] = "0b" + imm 


        elif instruction[25:] == "0010111":
            val = PC + signed_binary_to_decimal(imm)
            registers[rd] = "0b"+deci_to_bin(val,32)

        PC += 4
        print("u_type")
    #J-type 
    elif(instruction[25:] in J_type):
        rd = instruction[20:25]
        #imm = instruction[10:0:-1] + instruction[11] + instruction[19:11:-1] + instruction[0] + "0"
        imm = instruction[0] + instruction[12:20] + instruction[11] + instruction[1:11] + "0"
        registers[rd] = "0b" + deci_to_bin(PC + 4,32)
        val = imm 
        PC += signed_binary_to_decimal(val)
        print("j_type")
        
    
    OUT.write("0b" + deci_to_bin(PC,32) + " ")
    for i in registers:
        OUT.write(registers[i] + " ")
    OUT.write("\n")
    
    return PC
def main():
    # inp = sys.argv[1]
    # out = sys.argv[2]
    # F = open("s_test1", "r")
    mainfile = ["00000000000000000000010000110011",
"11111111100100000000010010010011",
"00000000000000010000010000110111",
"00000000100101000010000000100011",
"00000000000101001000010010010011",
"00000000010001000000010000010011",
"00000000100101000010000000100011",
"00000000000000010000010000010111",
"00000000000101001000010010010011",
"00000000100101000010000000100011",
"00000000010001000000010000010011",
"00000000000101001000010010010011",
"00000000100101000010000000100011",
"00000000000000000000000001100011"]
    # for line in F:
    #     if line != "" and line != "\n":
    #         mainfile.append(line)

    # F.close()

    flag = 1

    PC = 0

    OUT = open("output.txt", "w")
    count = 0

    #line_no = PC//4
    #print(line_no)
    
    if len(mainfile) <= 128:
        while (mainfile[PC//4] != "00000000000000000000000001100011" and PC//4 < len(mainfile)):
            print(mainfile[PC//4])
            count += 1
            print(count ,"    count")
            PC = simulator(mainfile[PC//4],PC,OUT)
            print(PC)
            # if count == 8:
            #     break
            # if PC == 44:
            #     PC = simulator(mainfile[PC//4],PC,OUT)
            #     print(PC)
            #     break
            
        # OUT.write("0b" + deci_to_bin(PC,32) + " ")
        # for i in registers:
        #     OUT.write(registers[i] + " ")
        # OUT.write("\n")

        for a in dataMemory:
            OUT.write(a + ":" + dataMemory[a])
            OUT.write("\n")           
        
    else:
        print("NO OF INSTRUCTIONS EXCEED 128")
    OUT.close()


if __name__ == "__main__":
    main()

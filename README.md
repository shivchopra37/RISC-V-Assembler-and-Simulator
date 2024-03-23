# Assembler

This is a simple assembler implemented in Python. It converts assembly language instructions into machine code for given architecture.

## Features

- Supports R-type, I-type, S-type, B-type, U-type, and J-type instructions.
- Handles labels and variables in the assembly code.
- Outputs the generated machine code to a specified file.

## Usage

1. **Input File**: Provide the assembly code in a text file. Each instruction should be written on a separate line.
   
2. **Output File**: Specify the file where you want to save the generated machine code.

3. **Run the Script**:

bash
python assembler.py <input_file> <output_file>


Replace `<input_file>` with the path to your assembly code file and `<output_file>` with the desired name for the output file.

## Supported Instructions

The assembler supports the following RISC-V instructions:

- R-type: `add`, `sub`, `sll`, `slt`, `sltu`, `xor`, `srl`, `or`, `and`
- I-type: `lw`, `addi`, `sltiu`, `jalr`
- S-type: `sw`
- B-type: `beq`, `bne`, `blt`, `bge`, `bltu`, `bgeu`
- U-type: `lui`, `auipc`
- J-type: `jal`

## Handling Labels

You can use labels in your assembly code to mark specific locations. Labels cannot be used as instructions. Here's how to use labels:

assembly
label:
    addi x1, x2, 10


## Handling Variables

Variables can be used in your assembly code. Ensure variables are declared and initialized before use.

## File Structure

- `assembler.py`: The main Python script containing the assembler logic.
- `input.asm`: Example input file with assembly code.
- `output.txt`: Example output file with generated machine code.

## Dependencies

This project doesn't have any external dependencies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute to this project by opening issues or pull requests. Any improvements or suggestions are welcome!
[![Typing SVG](https://readme-typing-svg.demolab.com/CO+PROJECT=First+line+of+text;Second+line+of+text)](https://git.io/typing-svg)

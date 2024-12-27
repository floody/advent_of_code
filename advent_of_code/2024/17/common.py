import re


def _decode_operand(operand, registers):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]
        case 7:
            raise ValueError("Operand is 7")


def _execute(program: list[int], registers: dict[str, int]):
    output = []
    program_counter = 0
    while program_counter < len(program):
        instruction = program[program_counter]
        operand = program[program_counter + 1]
        program_counter += 2
        match instruction:
            case 0:
                registers["A"] = registers["A"] // 2 ** _decode_operand(
                    operand, registers
                )
            case 1:
                registers["B"] ^= operand
            case 2:
                registers["B"] = _decode_operand(operand, registers) % 8
            case 3:
                if registers["A"]:
                    program_counter = operand
            case 4:
                registers["B"] ^= registers["C"]
            case 5:
                output.append(_decode_operand(operand, registers) % 8)
            case 6:
                registers["B"] = registers["A"] // 2 ** _decode_operand(
                    operand, registers
                )
            case 7:
                registers["C"] = registers["A"] // 2 ** _decode_operand(
                    operand, registers
                )

    return registers, output


def _parse_puzzle(puzzle):
    register_a = re.compile(r"Register A: ([0-9]+)")
    register_b = re.compile(r"Register B: ([0-9]+)")
    register_c = re.compile(r"Register C: ([0-9]+)")
    program = re.compile(r"Program: ([0-9,]+)")

    registers = {}

    for i in range(5):
        line = puzzle.readline()
        match i:
            case 0:
                registers["A"] = int(register_a.match(line).group(1))
            case 1:
                registers["B"] = int(register_b.match(line).group(1))
            case 2:
                registers["C"] = int(register_c.match(line).group(1))
            case 4:
                return [
                    int(s) for s in program.match(line).group(1).split(",")
                ], registers

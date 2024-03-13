from isa import ISA, CallInstruction, HaltInstruction, JumpInstruction


class Processor:
    class UnknownOpcode(Exception):
        pass

    def __init__(self, memory, stack, call_stack, ISA=ISA, debug=False):
        self._memory = memory.data
        self._user_memory = None
        self.pc = 0
        self.stack = stack
        self.call_stack = call_stack
        self._debug = debug
        self.instructions = {i.opcode: i(self) for i in ISA}

    def _fetch(self):
        return self._memory[self.pc]

    @staticmethod
    def _decode(instruction):
        return (
            instruction >> 0b10000,
            instruction & 0b1111111111111111,
        )

    def _get_instruction_name(self, opcode):
        return self.instructions[opcode].name

    def _execute(self, opcode, operand=0):
        if self._debug:
            print("Stack:")
            self.stack.pprint()
            instruction_name = self._get_instruction_name(opcode)
            print(
                f"Executing line {self.pc}: {instruction_name}({bin(opcode)}) {bin(operand)}"
            )
        result = self.instructions[opcode].execute(operand)
        if opcode not in [JumpInstruction.opcode, CallInstruction.opcode]:
            self.pc += 1
        return result

    def run(self, program, debug=False):
        program_len = len(program)
        self._memory[:program_len] = program
        self._user_memory = program_len
        self._debug = debug
        if self._debug:
            print("Running instructions:")
            print([bin(instruction) for instruction in program])
            print(f"Program size {len(program) * 21} bits")
        while True:
            try:
                instruction = self._fetch()
                opcode, operand = self._decode(instruction)
                self._execute(opcode, operand)
            except HaltInstruction.Halt:
                break

    def set_address(self, address, value):
        self._memory[self._user_memory + address] = value

    def get_address(self, address):
        return self._memory[self._user_memory + address]

    def print_program(self):
        print([hex(line) for line in self._memory])

import sys
from compiler import compile_rfl
from memory import Memory, Stack
from processor import Processor

if __name__ == "__main__":
    memory = Memory(32)  # create a memory with 32 bytes
    stack = Stack(8)  # create a stack with 8 bytes
    call_stack = Stack(8)  # create a call stack with 8 bytes

    # create a processor with the memory, stack and call stack
    processor = Processor(memory=memory, stack=stack, call_stack=call_stack)

    try:
        rfl_file = sys.argv[1]
    except IndexError:
        print(
            "Error: the program path should be passed. Ex. python main.py 'program.rfl'"
        )
    else:
        # compile program file
        program = compile_rfl(rfl_file, debug=False)

        # run the program
        processor.run(program, debug=False)

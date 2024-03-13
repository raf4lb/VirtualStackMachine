from compiler import compile_rfl
from memory import Memory, Stack
from processor import Processor

if __name__ == "__main__":
    memory = Memory(32)  # create a memory with 32 bytes
    stack = Stack(8)  # create a stack with 8 bytes
    call_stack = Stack(8)  # create a call stack with 8 bytes

    # create a processor with the memory, stack and call stack
    processor = Processor(
        memory=memory,
        stack=stack,
        call_stack=call_stack
    )

    # complile program in file "programs/for.rfl"
    program = compile_rfl("programs/for_commented.rfl", debug=False)

    # run the program
    processor.run(program, debug=False)

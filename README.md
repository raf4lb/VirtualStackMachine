# Simple Virtual Stack Machine
**Disclaimer**: despite being a project that works, it is still under development to add new features and improvements.

### Description
This is a simple virtual stack machine implemented in pure python. It has its own assembly language, compiler and the current instructions supported are:

##### Stack operations
- Push literal: push a value to the stack;
  - PSHL [value]
- Push: push a value from an address to the stack;
  - PSH [address] or $[variable_name]
- Pop: pop a value from the stack and stores it in the address;
  - POP [address] or $[variable_name]
- Top: print the value stored at the top of the stack;
  - TOP
##### Arithmetic operations
- Addition: add the two last values of the stack and stores the result at the top of the stack;
  - ADD
- Subtracttion: subtract the two last values of the stack and stores the result at the top of the stack;
  - SUB
- Multiplication: multiply the two last values of the stack and stores the result at the top of the stack;
  - MUL
- Division: divide the two last values of the stack and stores the result at the top of the stack;
  - DIV
##### Loop and Branching operations
- Jump (address): jump to address;
  - JMP [address] or .[label_name]
- Jump equal (address): jump to the next line if the value of the top of the stack is equal to the given address value;
  - JE [address] or $[variable_name]
- Jump less (address): jump to the next line if the value of the top of the stack is less than the given address value;
  - JL [address] or $[variable_name]
- Jump greater (address): jump to the next line if the value of the top of the stack is greater than the given address value;
  - JG [address] or $[variable_name]
- Jump less equal (address): jump to the next line if the value of the top of the stack is less or equal to the given address value;
  - JLE [address] or $[variable_name]
- Jump greater equal (address): jump to the next line if the value of the top of the stack is greater or equal to the given address value;
  - JGE [address] or $[variable_name]
- Call (address): call routine at address;
  - CALL [address] or .[label_name]
- Return: return to the program flow;
  - RET
##### Other instructions
- Variable declaration: variables can be used in push (PSH) pop (POP) instructions;
  - VAR [variable_name]
- Label declaration: labels can be used in jump (JMP) instruction;
  -  .[label_name]
- Halt: end the program;
  - HLT
- Delay (milliseconds): wait for milliseconds;
  - DLY [milliseconds]

### Requirements
 - Python 3.10;
 
### Installing
Clone this repo.

### Executing Programs
To execute a program in the VM, run the following command in the project root folder:
```
python main.py <path_to_program.rfl>
```
There are some commented programs examples in the ```programs``` folder. Example:
```
python main.py programs/for.rfl
```

### Project Structure
- ```programs``` folder contains program examples in the VM assembly code;
- ```alu.py``` contains the class that represents the arithmetic logic unit;
- ```compiler.py``` contains the compiler responsible for converting assembly code to VM bytecode;
- ```isa.py``` contains all VM instructions that can be easily extented using the ```Instruction``` abstract class;
- ```main.py``` contains the main script to compile and run the VM bytecode;
- ```memory.py``` contains classes related to memory elements like memory and stack;
- ```processor.py``` contains the class that represents the processor.

### Related Projects
There is an implementation of this VM in C, so the same assembly code can be executed even in baremetal microcontrollers like arduino with support to PIN manipulations (see atmega328p branch):

https://github.com/raf4lb/RFLVirtualStackMachineC

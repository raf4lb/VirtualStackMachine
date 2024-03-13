import time
from abc import ABC, abstractmethod

from alu import ALU


class Instruction(ABC):

  def __init__(self, processor):
    self.processor = processor

  @property
  @abstractmethod
  def name(self):
    ...

  @property
  @abstractmethod
  def opcode(self):
    ...

  @abstractmethod
  def execute(self, *args, **kwargs):
    ...


class HaltInstruction(Instruction):
  name = "HLT"
  opcode = 0b0

  class Halt(Exception):
    pass

  def execute(self, operand=None):
    raise self.Halt


class PushInstruction(Instruction):
  name = "PSH"
  opcode = 0b1

  def execute(self, address):
    self.processor.stack.push(self.processor.get_address(address))


class PushLiteralInstruction(Instruction):
  name = "PSHL"
  opcode = 0b1111

  def execute(self, value):
    self.processor.stack.push(value)


class PopInstruction(Instruction):
  name = "POP"
  opcode = 0b10

  def execute(self, address):
    self.processor.set_address(address, self.processor.stack.pop())


class AddInstruction(Instruction):
  name = "ADD"
  opcode = 0b11

  def execute(self, operand=None):
    b = self.processor.stack.pop()
    a = self.processor.stack.pop()
    result = ALU.add(a, b)
    self.processor.stack.push(result)


class SubtractInstruction(Instruction):
  name = "SUB"
  opcode = 0b100

  def execute(self, operand=None):
    b = self.processor.stack.pop()
    a = self.processor.stack.pop()
    result = ALU.subtract(a, b)
    self.processor.stack.push(result)


class MultiplyInstruction(Instruction):
  name = "MUL"
  opcode = 0b101

  def execute(self, operand=None):
    b = self.processor.stack.pop()
    a = self.processor.stack.pop()
    result = ALU.multiply(a, b)
    self.processor.stack.push(result)


class DivideInstruction(Instruction):
  name = "DIV"
  opcode = 0b110

  def execute(self, operand=None):
    b = self.processor.stack.pop()
    a = self.processor.stack.pop()
    result = ALU.divide(a, b)
    self.processor.stack.push(result)


class TopInstruction(Instruction):
  name = "TOP"
  opcode = 0b111

  def execute(self, operand=None):
    print(self.processor.stack.get_top())


class JumpInstruction(Instruction):
  name = "JMP"
  opcode = 0b1000

  def execute(self, address):
    self.processor.pc = address
    


class JumpEqualInstruction(Instruction):
  name = "JE"
  opcode = 0b1001

  def execute(self, address):
    if self.processor.stack.get_top() == self.processor.get_address(address):
      self.processor.pc += 1


class JumpLessInstruction(Instruction):
  name = "JL"
  opcode = 0b1010

  def execute(self, address):
    if self.processor.stack.get_top() < self.processor.get_address(address):
      self.processor.pc += 1


class JumpGreaterInstruction(Instruction):
  name = "JG"
  opcode = 0b1011

  def execute(self, address):
    if self.processor.stack.get_top() > self.processor.get_address(address):
      self.processor.pc += 1


class JumpLessEqualInstruction(Instruction):
  name = "JLE"
  opcode = 0b1100

  def execute(self, address):
    if self.processor.stack.get_top() <= self.processor.get_address(address):
      self.processor.pc += 1


class JumpGreaterEqualInstruction(Instruction):
  name = "JGE"
  opcode = 0b1101

  def execute(self, address):
    if self.processor.stack.get_top() >= self.processor.get_address(address):
      self.processor.pc += 1


class DelayInstruction(Instruction):
  name = "DLY"
  opcode = 0b1110

  def execute(self, value):
    time.sleep(value / 1000)


class CallInstruction(Instruction):
  name = "CALL"
  opcode = 0b10000

  def execute(self, address):
    self.processor.call_stack.push(self.processor.pc)
    self.processor.pc = address


class ReturnInstruction(Instruction):
  name = "RET"
  opcode = 0b10001

  def execute(self, operand=None):
    address = self.processor.call_stack.pop()
    self.processor.pc = address

ISA = [
    HaltInstruction,
    PushInstruction,
    PushLiteralInstruction,
    PopInstruction,
    AddInstruction,
    SubtractInstruction,
    MultiplyInstruction,
    DivideInstruction,
    TopInstruction,
    JumpInstruction,
    JumpEqualInstruction,
    JumpLessInstruction,
    JumpGreaterInstruction,
    JumpLessEqualInstruction,
    JumpGreaterEqualInstruction,
    DelayInstruction,
    CallInstruction,
    ReturnInstruction
]

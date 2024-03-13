class Memory:

  def __init__(self, size):
    self.size = size
    self.data = [0] * size


class Stack(Memory):

  def __init__(self, size):
    super().__init__(size)
    self._sp = 0

  def push(self, value):
    self.data[self._sp] = value
    self._sp += 1

  def pop(self):
    self._sp -= 1
    return self.data[self._sp]

  def pprint(self):
    output = [str(v) for v in self.data]
    output[self._sp] = f"->{output[self._sp]}"
    print("[", ", ".join(output), "]")

  def get_top(self):
    return self.data[self._sp - 1]

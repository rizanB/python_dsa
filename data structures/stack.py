
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-final-newline


from typing import List


class Stack:
    def __init__(self) -> None:
        self.stack: List[object] = []

    def __repr__(self) -> str:

        result: str = f"Length: {len(self.stack)}\n"

        if self.is_empty():
            result += "stack is empty"

        else:
            result += f"item: {self.stack[:: -1]}\n"

        return result

    def push(self, value: object):
        self.stack.append(value)

    def peek(self):
        return self.stack[-1]

    def is_empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self) -> int:
        return len(self.stack)

    def pop(self):
        if self.is_empty():
            return "cannot pop, stack is empty"
        else:
            return self.stack.pop()


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack)

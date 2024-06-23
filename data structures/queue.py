# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-final-newline

from typing import List


class Queue:
    def __init__(self, front: int = 0, back: int = 0) -> None:
        self.my_queue: List[int] = []
        self.front = front
        self.back = back

    def __repr__(self) -> str:
        if self.is_empty():
            return "empty queue"
        else:
            value = ""
            for i in range(self.front, self.back):
                value += f"{self.my_queue[i]} \n"
            return value

    def is_empty(self) -> bool:
        return self.front == self.back

    def enqueue(self, value: int):
        self.my_queue.append(value)
        self.back += 1

    def dequeue(self):
        if self.is_empty():
            return "cannot dequeue, queue is empty"

        else:
            value: int = self.my_queue[self.front]
            self.front += 1
            return value

    def peek(self):
        if self.is_empty():
            return "queue is empty"
        else:
            return self.my_queue[self.front]


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
print(q)
print(q.peek())

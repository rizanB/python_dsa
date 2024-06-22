# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-final-newline

# Linked list : node1 -> node2 ->  None

class Node:
    def __init__(self, value: int, next_node: 'Node | None') -> None:
        self.value = value
        self.next_node = next_node

    def __repr__(self) -> str:
        return f"value: {self.value}, next node: {self.next_node}"


node1 = Node(1, None)


class LinkedList:
    def __init__(self, head: 'None | Node') -> None:
        self.head = head

    def __repr__(self) -> str:
        result: str = f"Length: {self.length()} \n"

        if self.head is None:
            result += "linked list is empty"

        else:
            current = self.head
            count: int = 1
            while current:
                result += f"Node {count} | value: {current.value}\n"
                count += 1
                current = current.next_node

        return result

    def append(self, value: int):
        current = self.head

        if current is None:
            new_node = Node(value, None)
            self.head = new_node

        else:
            while current.next_node:
                current = current.next_node
            new_node = Node(value, None)
            current.next_node = new_node

    def length(self) -> int:
        current = self.head
        count: int = 0
        while current:
            current = current.next_node
            count += 1

        return count


my_linked_list = LinkedList(node1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print(my_linked_list)

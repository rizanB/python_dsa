# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-final-newline


class Node:
    def __init__(self, value: 'int', left: 'Node | None' = None, right: 'Node | None' = None) -> None:
        self.value = value
        self.left = left
        self.right = right
        
class Tree:
    def __init__(self, root: 'None | Node' = None) -> None:
        self.root = root
        
        
    def insert(self, value_to_insert: int):
        
        if self.root is None:
            self.root = Node(value_to_insert)
            
        else:
            self._insert_into_subtree_recursive(self.root, value_to_insert)
            
    def _insert_into_subtree_recursive(self, node: Node, value_to_insert: int):
        if value_to_insert < node.value:
            if node.left is None:
                node.left = Node(value_to_insert)
            else:
                self._insert_into_subtree_recursive(node.left, value_to_insert)
                
        elif value_to_insert > node.value:
            
            if node.right is None:
                node.right = Node(value_to_insert)
                
            else:
                self._insert_into_subtree_recursive(node.right, value_to_insert)
                

my_tree = Tree()

my_tree.insert(5)
my_tree.insert(3)
my_tree.insert(7)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)

print(my_tree.root.left.left.value)
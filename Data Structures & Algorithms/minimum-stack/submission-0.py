class Node:
    def __init__(self, val: int, prev_node: Node = None):
        self.val = val
        self.prev_node = prev_node


class Stack:

    def __init__(self):
        self.tail = None

    def is_empty(self) -> bool:
        return self.tail is None

    def push(self, val: int) -> None:
        node = Node(val, self.tail)
        if self.tail is not None:
            self.tail.next_node = Node
        self.tail = node

    def pop(self) -> None:
        old_tail = self.tail
        self.tail = self.tail.prev_node
        old_tail.prev_node = None

    def top(self) -> int:
        return self.tail.val


class MinStack:

    def __init__(self):
        self.val_stack = Stack()
        self.min_stack = Stack()

    def push(self, val: int) -> None:
        self.val_stack.push(val)
        if self.min_stack.is_empty():
            self.min_stack.push(val)
        else:
            self.min_stack.push(min(self.min_stack.top(), val))

    def pop(self) -> None:
        self.val_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.val_stack.top()

    def getMin(self) -> int:
        return self.min_stack.top()
